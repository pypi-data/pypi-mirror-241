import statistics
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, Any, cast, Union
from uuid import UUID

import dacite
from dacite import from_dict
from flask import Blueprint, abort, redirect, render_template, g, request, jsonify
from flask.typing import ResponseReturnValue
from sqlalchemy import select

from freeplay_server.accounts.users import Roles
from freeplay_server.auth.auth_filter import allow_role
from freeplay_server.evaluations.eval_page import EvaluationCriteriaInfo
from freeplay_server.extensions import sa
from freeplay_server.models import TestList, TestRun, ProjectSession, EvaluationCriteria, PromptTemplate
from freeplay_server.project_sessions.project_sessions_repository import ProjectSessionsRecord, \
    ProjectSessionsRepository
from freeplay_server.projects.project_page_blueprint_filters import ProjectPageBlueprintFilters
from freeplay_server.prompt_templates.prompt_template_version_repository import PromptTemplateVersion, \
    PromptTemplateVersionRepository
from freeplay_server.test_lists.test_lists_repository import TestListsRepository, TestListFields, \
    TestListRecord, TestListPersistenceFailure, TestCaseRecord, TestCaseUpload
from freeplay_server.test_runs.test_runs_service import TestRunListRecord, TestRunsService, \
    MostCommonFirstTemplateVersion
from freeplay_server.utilities.formatters import format_decimal_dollars, format_latency
from freeplay_server.utilities.http_constants import ContentType
from freeplay_server.utilities.render_react import render_react
from freeplay_server.web_support import json_support
from freeplay_server.web_support.form_support import try_decode_form


@dataclass
class SessionCollectionInfo:
    total_cost: Optional[str]
    mean_latency: Optional[str]
    mean_cost: Optional[str]

    def __init__(self, sessions: list[ProjectSession]):
        session_costs = []
        session_latencies = []
        for session in sessions:
            session_latencies.append(session.latency())
            session_costs.append(session.cost())

        # Summing over a Decimal requires an initial /decimal/ value to avoid type issues with this becoming int|decimal
        self.total_cost = format_decimal_dollars(sum(session_costs, Decimal(0))) if len(session_costs) else None
        self.mean_cost = format_decimal_dollars(statistics.mean(session_costs)) if len(session_costs) else None
        self.mean_latency = format_latency(statistics.mean(session_latencies)) if len(session_latencies) else None


@dataclass
class TestListInfo:
    id: UUID
    name: str
    test_list_id: UUID
    description: Optional[str]
    delete_url: str
    update_url: str
    details_url: str
    is_deleted: bool
    most_common_first_prompt_name: Optional[str]
    test_case_count: Optional[int]

    def __init__(
            self,
            record: Union[TestListRecord, TestList],
            most_common_first_prompt_name: Optional[str] = None,
            test_case_count: Optional[int] = None
    ):
        self.id = record.id
        self.name = record.name
        self.description = record.description
        self.test_list_id = record.id
        self.most_common_first_prompt_name = most_common_first_prompt_name
        self.delete_url = f'/projects/{record.project_id}/test_lists/{record.id}/delete'
        self.update_url = f'/projects/{record.project_id}/test_lists/{record.id}/update'
        self.details_url = f'/projects/{record.project_id}/test_lists/{record.id}'
        self.is_deleted = bool(record.deleted_at)
        self.test_case_count = test_case_count


@dataclass
class TestRunListInfo:
    id: UUID
    created_at: int
    test_list_info: Optional[TestListInfo]
    details_url: str
    prompt_name: Optional[str]
    prompt_version_timestamp: Optional[int]
    prompt_version_url: Optional[str]
    prompt_model_name: Optional[str]
    session_collection_info: Optional[SessionCollectionInfo]
    eval_criteria_summary: Optional[dict[str, str]]

    def __init__(
            self,
            test_run_record: Union[TestRunListRecord, TestRun],
            test_list_info: Optional[TestListInfo],
            template_version: Optional[MostCommonFirstTemplateVersion],
            session_collection_info: Optional[SessionCollectionInfo] = None,
            eval_criteria_summary: Optional[dict[str, str]] = None
    ):
        if isinstance(test_run_record, TestRunListRecord):
            project_id = test_run_record.project_id
        else:
            project_id = test_run_record.test_list.project_id

        self.id = test_run_record.id
        self.created_at = int(test_run_record.created_at.timestamp())
        self.test_list_info = test_list_info
        self.details_url = f'/projects/{project_id}/test_runs/{test_run_record.id}'
        self.prompt_name = template_version.name if template_version else None
        self.prompt_model_name = template_version.model_name if template_version else None
        self.prompt_version_timestamp = int(template_version.created_at.timestamp()) if template_version else None
        self.details_url = f'/projects/{project_id}/test_runs/{test_run_record.id}'
        self.session_collection_info = session_collection_info
        self.eval_criteria_summary = eval_criteria_summary

        if template_version:
            self.prompt_version_url = f'/projects/{project_id}/templates/{template_version.prompt_template_id}/versions/{template_version.prompt_template_version_id}'
        else:
            self.prompt_version_url = None


@dataclass
class TestCaseInfo:
    inputs: dict[str, str]
    output: str
    delete_url: str
    source: str
    created_from_session_url: Optional[str]

    def __init__(self, record: TestCaseRecord, test_list_id: UUID, project_id: UUID,
                 session: Optional[ProjectSessionsRecord], ptv: Optional[PromptTemplateVersion]):
        self.inputs = record.inputs
        self.output = session.response if session else record.uploaded_output or ''
        self.delete_url = f'/projects/{project_id}/test_lists/{test_list_id}/test_cases/{record.id}/delete'
        self.created_from_session_url = f'/projects/{project_id}/sessions/{record.created_from_session_id}' if record.created_from_session_id else None
        self.source = str(ptv.name) if ptv else 'Upload'


def test_lists_page(
        filters: ProjectPageBlueprintFilters,
        repo: TestListsRepository,
        test_runs_service: TestRunsService,
        project_sessions_repo: ProjectSessionsRepository,
        prompt_template_version_repo: PromptTemplateVersionRepository,
        api_url: str) -> Blueprint:
    page = Blueprint('test_lists_page', __name__, url_prefix='/projects/<project_id>')

    @page.url_value_preprocessor
    def hydrate_projects(_: Optional[str], values: Optional[dict[str, Any]]) -> None:
        filters.hydrate_projects(values)

    @page.before_request
    def before_request() -> Optional[ResponseReturnValue]:
        return filters.before_page_request()

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/tests')
    def index() -> ResponseReturnValue:
        test_run_list_infos = []

        evaluation_criteria = sa.session.execute(
            select(EvaluationCriteria).join(PromptTemplate, EvaluationCriteria.prompt_template_id == PromptTemplate.id)
            .where(PromptTemplate.project_id == g.project.id)
        ).scalars().all()

        for test_run in test_runs_service.find_all_by_project_with_sessions(g.project.id):
            prompt_template_version = test_runs_service.most_common_first_template_version(test_run.id)
            # noinspection PyTypeChecker
            # TestList is correctly typed but MyPy is not correctly inferring SqlAlchemy types.
            test_list_info = TestListInfo(
                test_run.test_list,
                prompt_template_version.name if prompt_template_version else None
            ) if test_run.test_list else None
            session_collection_info = SessionCollectionInfo(test_run.project_sessions)
            eval_criteria_output = test_runs_service.summarize_test_run_evals(test_run, list(evaluation_criteria))

            test_run_list_infos.append(
                TestRunListInfo(
                    test_run,
                    test_list_info,
                    prompt_template_version,
                    session_collection_info,
                    eval_criteria_output
                )
            )

        test_lists = repo.find_all_by_project_id(g.project.id)
        test_list_infos = [TestListInfo(tl, test_case_count=tl.num_test_cases()) for tl in test_lists]

        return render_react(
            'TestRunsListPage',
            title='Test Lists',
            test_lists=test_list_infos,
            evaluation_criteria=[EvaluationCriteriaInfo(ec) for ec in evaluation_criteria],
            test_runs=test_run_list_infos,
            api_url=api_url,
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/test_lists/<uuid:test_list_id>')
    def show_test_list(test_list_id: UUID) -> ResponseReturnValue:
        test_list = repo.try_find(test_list_id)
        if not test_list:
            abort(404)

        test_cases = repo.find_test_cases_for_test_list(test_list.id)

        sessions = project_sessions_repo.find_all_by_ids(
            [tc.created_from_session_id for tc in test_cases if tc.created_from_session_id is not None])
        sessions_by_id = {session.id: session for session in sessions}
        prompt_templates_by_id = prompt_template_version_repo.find_template_version_by_ids(
            [session.prompt_template_version_id for session in sessions])
        test_case_infos = []
        for test_case in test_cases:
            session = sessions_by_id.get(test_case.created_from_session_id,
                                         None) if test_case.created_from_session_id else None
            ptv = prompt_templates_by_id.get(session.prompt_template_version_id, None) if session else None
            test_case_infos.append(TestCaseInfo(test_case, test_list.id, g.project.id, session, ptv))

        # Find the first project session entry that matches the first session, grab the template name.
        first_template_name = None
        for test_case in test_cases:
            if not test_case.created_from_session_id:
                continue
            session_details = project_sessions_repo.try_find(test_case.created_from_session_id)
            if session_details is not None and len(session_details.entries) > 0:
                first_template_name = session_details.entries[0].template_name
                break

        return render_react(
            'TestListShowPage',
            title=f'Test List: {test_list.name}',
            project_id=g.project.id,
            test_cases=test_case_infos,
            test_list=TestListInfo(test_list, first_template_name),
            first_prompt_template_name=first_template_name,
            api_url=api_url,
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/test_lists/new')
    def new() -> ResponseReturnValue:
        return render_template(
            'test_lists_page/new.html',
            name='',
            create_url=f'/projects/{g.project.id}/test_lists',
            cancel_url=f'/projects/{g.project.id}/tests'
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/test_lists')
    def create() -> ResponseReturnValue:
        if request.content_type == ContentType.APPLICATION_JSON:
            return __create_test_list_json()
        else:
            return __create_test_list_form_data()

    def __create_test_list_form_data() -> ResponseReturnValue:
        def render_error(error_message: str) -> ResponseReturnValue:
            return render_template(
                'test_lists_page/new.html',
                error_message=error_message,
                name=request.form.get('name', ''),
                create_url=f'/projects/{g.project.id}/test_lists',
                cancel_url=f'/projects/{g.project.id}/tests'
            ), 400

        fields = try_decode_form(TestListFields)
        if fields is None:
            return render_error(
                error_message='Form was incomplete',
            )

        result = repo.create(g.project.id, fields)

        if type(result) is TestListPersistenceFailure:
            return render_error(
                error_message=result.value
            )

        return redirect(f'/projects/{g.project.id}/tests')

    def __create_test_list_json() -> ResponseReturnValue:
        json_fields = from_dict(TestListFields, request.get_json())

        result = repo.create(g.project.id, json_fields)

        if type(result) is TestListPersistenceFailure:
            response = jsonify({"message": result.value})
            response.status_code = 400
            return response

        return jsonify(TestListInfo(cast(TestListRecord, result))), 201

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/test_lists/<uuid:test_list_id>/update')
    def show_update(test_list_id: UUID) -> ResponseReturnValue:
        test_list = repo.try_find(test_list_id)
        if not test_list:
            abort(404)

        return render_template(
            'test_lists_page/update.html',
            name=test_list.name,
            description=test_list.description,
            update_url=f'/projects/{g.project.id}/test_lists/{test_list.id}/update',
            cancel_url=f'/projects/{g.project.id}/test_lists/{test_list.id}'
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/test_lists/<uuid:test_list_id>/update')
    def update(test_list_id: UUID) -> ResponseReturnValue:
        test_list = repo.try_find(test_list_id)
        if not test_list:
            abort(404)

        def render_error(error_message: str) -> ResponseReturnValue:
            return render_template(
                'test_lists_page/update.html',
                error_message=error_message,
                name=request.form.get('name', ''),
                description=request.form.get('description', ''),
                update_url=f'/projects/{g.project.id}/test_lists/{test_list.id}/update',
                cancel_url=f'/projects/{g.project.id}/tests'
            ), 400

        fields = try_decode_form(TestListFields)
        if fields is None:
            return render_error(
                error_message='Form was incomplete',
            )

        result = repo.update(g.project.id, test_list.id, fields)

        if type(result) is TestListPersistenceFailure:
            return render_error(
                error_message=result.value
            )

        return redirect(f'/projects/{g.project.id}/test_lists/{test_list.id}')

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/test_lists/<uuid:test_list_id>/delete')
    def destroy_test_list(test_list_id: UUID) -> ResponseReturnValue:
        repo.soft_delete_test_list(test_list_id)

        return redirect(f'/projects/{g.project.id}/tests')

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/test_lists/<uuid:test_list_id>/test_cases/<uuid:test_case_id>/delete')
    def destroy_test_case(test_list_id: UUID, test_case_id: UUID) -> ResponseReturnValue:
        test_list = repo.try_find(test_list_id)
        if test_list is None:
            return redirect(f'/projects/{g.project.id}/tests')
        repo.delete_test_case_from_test_list(test_list.id, test_case_id)
        return redirect(f'/projects/{g.project.id}/test_lists/{test_list.id}')

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/test_lists/<uuid:test_list_id>/upload')
    def upload_test_cases(test_list_id: UUID) -> ResponseReturnValue:
        if 'file' not in request.files:
            abort(400, 'No file part')
        file = request.files['file']

        test_list = repo.try_find(test_list_id)
        if not test_list:
            raise RuntimeError('Test list not found')

        test_cases: list[TestCaseUpload] = []
        for line in file:
            try:
                upload = json_support.force_decode(TestCaseUpload, line)
                test_cases.append(upload)
            except Exception:
                abort(400, 'Uploaded file was malformed')

        if not test_cases:
            abort(400, 'No valid inputs')

        try:
            repo.insert_uploaded_test_cases(test_list_id, test_cases)
        except Exception as e:
            if str(e) == 'Input keys do not match':
                abort(400,
                      'Invalid input: input keys for uploaded test cases must all be the same and be the same as existing inputs.')
            else:
                raise e

        return redirect(f'/projects/{g.project.id}/test_lists/{test_list_id}')

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/test_lists/add_sessions')
    def add_sessions() -> ResponseReturnValue:
        @dataclass
        class AddSessionsRequest:
            test_list_id: str
            session_ids: list[str]

        add_sessions_request = dacite.from_dict(AddSessionsRequest, request.get_json())
        test_list_id = UUID(add_sessions_request.test_list_id)
        session_ids = [UUID(id) for id in add_sessions_request.session_ids]
        sessions = project_sessions_repo.find_all_by_ids(session_ids)
        repo.add_sessions_to_test_list(test_list_id, sessions)
        return 'OK', 200

    return page
