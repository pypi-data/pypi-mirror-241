from dataclasses import dataclass
from typing import Optional, Any, cast
from urllib.parse import unquote, urlencode
from uuid import UUID

from dacite import from_dict
from flask import Blueprint, abort, redirect, g, request, jsonify
from flask.typing import ResponseReturnValue
from sqlalchemy import ScalarResult, delete, distinct, select
from sqlalchemy.dialects.postgresql import insert

from freeplay_server.accounts.users import Roles
from freeplay_server.auth.auth_filter import allow_role
from freeplay_server.evaluations.eval_page import EvaluationCriteriaInfo
from freeplay_server.extensions import sa
from freeplay_server.models import EvaluationCriteria, EvaluationResult, ProjectSession, ProjectSessionEntry, \
    ProjectSessionEntryInputs, PromptTemplate, Environment
from freeplay_server.project_sessions.project_sessions_repository import ProjectSessionsRepository, \
    SessionsDataRequest, FilterConfig
from freeplay_server.project_sessions.session_display_service import SessionDisplayService
from freeplay_server.projects.project_page_blueprint_filters import ProjectPageBlueprintFilters
from freeplay_server.prompt_templates.llm_model_repository import LLMModelRepository
from freeplay_server.prompt_templates.prompt_template_version_repository import PromptTemplateVersionRepository
from freeplay_server.test_lists.test_lists_page import TestListInfo
from freeplay_server.test_lists.test_lists_repository import TestListsRepository
from freeplay_server.utilities.render_react import render_react
from freeplay_server.web_support import json_support
from freeplay_server.web_support.api_support import try_parse_uuid
from freeplay_server.web_support.json_support import dacite_config


@dataclass
class ProjectSessionInfo:
    id: str
    start_time: int
    inputs: dict[str, str]
    response: str
    details_url: str
    prompt_names: list[str]
    models: list[str]
    providers: list[str]
    api_key_names: list[str]
    environments: list[str]
    # criteria name -> manual_score > auto_eval_score
    eval_results_combined: dict[str, Any]

    def __init__(self, session: ProjectSession, details_url: str) -> None:
        model_names = [e.model.name for e in session.entries if e.model]
        providers = [e.model.flavor.provider_name for e in session.entries if e.model]
        prompt_names = [e.prompt_template.name for e in session.entries if e.prompt_template_id]
        api_key_names = [e.api_key_name for e in session.entries if e.prompt_template_id and e.api_key_name]
        environments = [e.environment.name for e in session.entries if e.environment]

        self.id = str(session.id)
        self.start_time = int(session.start_time.timestamp())
        self.details_url = details_url
        self.inputs = session.entries[0].inputs_dict() if session.entries else {}
        self.response = session.entries[-1].response if session.entries else ''
        self.prompt_names = sorted(list(set(prompt_names)))
        self.models = sorted(list(set(model_names)))
        self.providers = sorted(list(set(providers)))
        self.api_key_names = sorted(list(set(api_key_names)))
        self.environments = sorted(list(set(environments)))
        self.eval_results_combined = {er.criterion.name: er.score() for er in
                                      session.evaluation_results}


@dataclass
class SessionEntryMetadata:
    template_name: str
    latency: Optional[str]
    cost: Optional[str]
    metadata_pairs: list[dict[str, str]]


def project_sessions_page(
        filters: ProjectPageBlueprintFilters,
        sessions_repo: ProjectSessionsRepository,
        test_list_repo: TestListsRepository,
        prompt_template_version_repo: PromptTemplateVersionRepository,
        llm_model_repo: LLMModelRepository,
        session_display_service: SessionDisplayService,
) -> Blueprint:
    page = Blueprint('sessions_page', __name__, url_prefix='/projects/<project_id>/sessions')

    @page.url_value_preprocessor
    def extract_project_id(_: Optional[str], values: Optional[dict[str, Any]]) -> None:
        filters.hydrate_projects(values)

    @page.before_request
    def before_request() -> Optional[ResponseReturnValue]:
        return filters.before_page_request()

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('')
    def index() -> ResponseReturnValue:
        environments_query = (
            select(Environment.name)
            .order_by(Environment.name.asc())
        )

        environments_names = list(set(sa.session.execute(environments_query).scalars()))
        filter_values = {
            'providers': ['openai', 'anthropic'],
            'models': llm_model_repo.model_names(),
            'prompt_names': prompt_template_version_repo.prompt_names(g.project.id),
            'environments': environments_names
        }
        project_criteria = sa.session.execute(
            select(EvaluationCriteria).join(PromptTemplate, EvaluationCriteria.prompt_template_id == PromptTemplate.id)
            .where(PromptTemplate.project_id == g.project.id)
        ).scalars()
        input_names = cast(ScalarResult[str], sa.session.execute(
            select(distinct(ProjectSessionEntryInputs.name)).join(
                ProjectSessionEntry, ProjectSessionEntryInputs.project_session_entry_id == ProjectSessionEntry.id
            ).join(
                ProjectSession, ProjectSessionEntry.project_session_id == ProjectSession.id
            ).filter(
                ProjectSession.project_id == g.project.id
                # Limit input names to the most recent 100k inputs
            ).limit(100000)
        ).scalars())

        return render_react(
            'SessionListPage',
            title='Project Sessions',
            sessions_empty=not sessions_repo.exist_session_entry_in_project(g.project.id),
            filter_values=filter_values,
            evaluation_criteria=[EvaluationCriteriaInfo(ec) for ec in project_criteria],
            input_names=list(input_names),
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/sessions_data')
    def sessions_data() -> ResponseReturnValue:
        data_request = from_dict(
            data_class=SessionsDataRequest,
            data=dict(request.get_json()),
            config=dacite_config())

        records = sessions_repo.find_project_session_list_records(g.project.id, data_request)
        sessions = [ProjectSessionInfo(record, f'/projects/{record.project_id}/sessions/{record.id}') for record in
                    records]
        row_count = sessions_repo.count_project_session_list_records(g.project.id, data_request.filters,
                                                                     data_request.before_datetime())
        return jsonify({'sessions': sessions, 'row_count': row_count})

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/<uuid:session_id>')
    def show_summary(session_id: UUID) -> ResponseReturnValue:
        filter_param = request.args.get('filters', None)
        filters = json_support.force_decode_dict(FilterConfig, unquote(filter_param).encode()) if filter_param else {}
        request_args = request.args.to_dict()
        test_list_id = None
        try:
            test_list_id = UUID(request_args.pop('test_list_id', None))
        except TypeError:
            pass

        session_info = session_display_service.get_session_display_info(session_id)
        if not session_info:
            abort(404)

        (prev, next) = sessions_repo.find_prev_next_sessions(g.project.id, filters, None, session_id)

        args_string = '?' + urlencode(request.args) if request.args else ''
        if test_list_id:
            test_cases = test_list_repo.find_test_cases_for_test_list(test_list_id)
            test_cases_session_ids = [
                test_case.created_from_session_id for test_case in test_cases
                if test_case.created_from_session_id
            ]
            (prev, next) = sessions_repo.find_prev_next_sessions(
                g.project.id, filters, None, session_id, test_cases_session_ids
            )
            close_url = f'/projects/{g.project.id}/test_lists/{test_list_id}'
        else:
            (prev, next) = sessions_repo.find_prev_next_sessions(g.project.id, filters, None, session_id)
            close_url = f'/projects/{g.project.id}/sessions{args_string}'

        previous_url = f'/projects/{g.project.id}/sessions/{prev.id}{args_string}' if prev is not None else None
        next_url = f'/projects/{g.project.id}/sessions/{next.id}{args_string}' if next is not None else None

        return render_react(
            'SessionDetailsPage',
            'Session details',
            close_url=close_url,
            created_at=session_info.created_at,
            session_id=session_info.session_id,
            session_groups=session_info.session_groups,
            session_overview=session_info.session_overview,
            evaluations=session_info.evaluations,
            test_lists=session_info.test_lists,
            show_action_buttons=True,
            previous_url=previous_url,
            next_url=next_url,
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/<uuid:session_id>/evaluations')
    def update_evaluation_result(session_id: UUID) -> ResponseReturnValue:
        form_value = request.form.get('manual_score')
        if form_value is None:
            return jsonify({'error': 'Score is required'}), 400
        [evaluation_criteria_id, score] = form_value.split('_')
        score_mapping = {
            'yes': 'yes',
            'no': 'no',
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
        }
        score_data = score_mapping.get(score)
        if score_data is None:
            return jsonify({'error': 'Score is malformed'}), 400

        sa.session.execute(insert(EvaluationResult).values(
            session_id=session_id,
            evaluation_criteria_id=evaluation_criteria_id,
            manual_score=score_data,
        ).on_conflict_do_update(
            index_elements=['evaluation_criteria_id', 'session_id'],
            set_=dict(manual_score=score_data),
        ))

        return redirect(request.referrer)

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/<uuid:session_id>/test_lists')
    def update_test_lists(session_id: UUID) -> ResponseReturnValue:
        test_list_uuids = [id for test_list_id in request.form.to_dict().keys() if (id := try_parse_uuid(test_list_id))]

        session = sessions_repo.try_find(session_id)
        if session is None:
            abort(404)

        test_list_repo.update_session_test_lists(session, test_list_uuids)
        args_string = '?' + urlencode(request.args) if request.args else ''
        return redirect(f'/projects/{g.project.id}/sessions/{session_id}{args_string}')

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/compatible_test_lists')
    def compatible_test_lists() -> ResponseReturnValue:
        input_keys = request.args.getlist('inputKey')
        test_lists = test_list_repo.get_compatible_test_lists(g.project.id, input_keys)

        test_list_infos = [TestListInfo(tl) for tl in test_lists]
        return jsonify(test_list_infos), 201

    @allow_role(Roles.ACCOUNT_USER)
    @page.delete("/<uuid:session_id>")
    def delete_session(session_id: UUID) -> ResponseReturnValue:
        session_details = sessions_repo.try_find(session_id)
        if session_details is None:
            return jsonify({'error': 'Not Found'}), 404

        sessions_repo.delete_session(session_id)
        return jsonify({})

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/delete_sessions')
    def delete_sessions() -> ResponseReturnValue:
        session_ids = request.form.to_dict().keys()
        sa.session.execute(delete(ProjectSession).where(ProjectSession.id.in_(session_ids)))
        args_string = '?' + urlencode(request.args) if request.args else ''
        return redirect(f'/projects/{g.project.id}/sessions{args_string}')

    return page
