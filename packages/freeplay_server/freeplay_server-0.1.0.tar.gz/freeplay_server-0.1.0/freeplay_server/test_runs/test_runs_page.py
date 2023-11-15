from typing import Optional, Any
from urllib.parse import unquote, urlencode
from uuid import UUID

from flask import Blueprint, abort, g, request, redirect
from flask.typing import ResponseReturnValue
from sqlalchemy import select, delete

from freeplay_server.accounts.users import Roles
from freeplay_server.auth.auth_filter import allow_role
from freeplay_server.evaluations.eval_page import EvaluationCriteriaInfo
from freeplay_server.extensions import sa
from freeplay_server.models import Environment, TestRun
from freeplay_server.project_sessions.project_sessions_page import ProjectSessionInfo
from freeplay_server.project_sessions.project_sessions_repository import ProjectSessionsRepository, FilterConfig
from freeplay_server.project_sessions.session_display_service import SessionDisplayService
from freeplay_server.projects.project_page_blueprint_filters import ProjectPageBlueprintFilters
from freeplay_server.test_lists.test_lists_page import TestRunListInfo, TestListInfo, SessionCollectionInfo
from freeplay_server.test_runs.test_runs_service import TestRunsService
from freeplay_server.utilities.render_react import render_react
from freeplay_server.web_support import json_support


def test_runs_page(
        filters: ProjectPageBlueprintFilters,
        test_runs_service: TestRunsService,
        project_sessions_repo: ProjectSessionsRepository,
        session_display_service: SessionDisplayService
) -> Blueprint:
    page = Blueprint('test_runs_page', __name__, url_prefix='/projects/<project_id>/test_runs')

    @page.url_value_preprocessor
    def hydrate_projects(_: Optional[str], values: Optional[dict[str, Any]]) -> None:
        filters.hydrate_projects(values)

    @page.before_request
    def before_request() -> Optional[ResponseReturnValue]:
        return filters.before_page_request()

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/<uuid:test_run_id>')
    def show_test_run_overview(test_run_id: UUID) -> ResponseReturnValue:
        test_run = sa.get_or_404(TestRun, test_run_id)
        prompt_template_version = test_runs_service.most_common_first_template_version(test_run_id)

        test_run_sessions = test_runs_service.find_test_run_sessions(test_run.id)
        criteria = [criterion for session in test_run_sessions for entry in session.entries for criterion in
                    entry.prompt_template.criteria]
        # Unique by id
        eval_criteria = list({criterion.id: EvaluationCriteriaInfo(criterion) for criterion in criteria}.values())
        test_run_unique_providers = project_sessions_repo.find_test_run_sessions_unique_providers(test_run_id)
        session_view_models = [
            ProjectSessionInfo(session, f'/projects/{session.project_id}/test_runs/{test_run_id}/sessions/{session.id}')
            for session in test_run_sessions]
        api_key_name = (
            test_run_sessions[0].entries[0].api_key_name
            if len(test_run_sessions) and len(test_run_sessions[0].entries) else None
        )
        environments_set = set()
        for test_run_session in test_run_sessions:
            for entry in test_run_session.entries:
                if entry.environment:
                    environments_set.add((entry.environment.name, entry.environment.is_deleted))

        environments = [{'name': x, 'is_deleted': y} for x, y in environments_set]
        environments_query = (
            select(Environment.name)
            .order_by(Environment.name.asc())
        )
        environments_names = list(sa.session.execute(environments_query).scalars())
        filter_values = {
            'environments': environments_names,
        }

        comparable_test_runs = sa.session.query(TestRun).where(
            TestRun.test_list_id == test_run.test_list.id
        ).filter(TestRun.id != test_run.id).order_by(TestRun.created_at.desc()).limit(100).all()

        comparable_test_run_infos = []
        for comparable_test_run in comparable_test_runs:
            comparable_test_run_infos.append(TestRunListInfo(
                comparable_test_run,
                TestListInfo(test_run.test_list),
                test_runs_service.most_common_first_template_version(comparable_test_run.id)
            ))

        return render_react(
            component='TestRunPage',
            title='Test Run',
            sessions=session_view_models,
            comparable_test_runs=comparable_test_run_infos,
            test_run=TestRunListInfo(test_run, TestListInfo(test_run.test_list), prompt_template_version),
            test_run_unique_providers=test_run_unique_providers,
            eval_criteria=eval_criteria,
            session_collection_info=SessionCollectionInfo(test_run_sessions),
            api_key_name=api_key_name,
            environments=environments,
            filter_values=filter_values,
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/<uuid:test_run_id>/sessions/<uuid:session_id>')
    def show_test_run_session(test_run_id: UUID, session_id: UUID) -> ResponseReturnValue:
        session_info = session_display_service.get_session_display_info(session_id)
        if not session_info:
            abort(404)

        filter_param = request.args.get('filters', None)
        filters = json_support.force_decode_dict(FilterConfig, unquote(filter_param).encode()) if filter_param else {}

        (prev, next) = project_sessions_repo.find_prev_next_sessions(g.project.id, filters, test_run_id,
                                                                     session_id)
        args_string = '?' + urlencode(request.args) if request.args else ''
        close_url = f'/projects/{g.project.id}/test_runs/{test_run_id}{args_string}'
        previous_url = f'/projects/{g.project.id}/test_runs/{test_run_id}/sessions/{prev.id}{args_string}' if prev is not None else None
        next_url = f'/projects/{g.project.id}/test_runs/{test_run_id}/sessions/{next.id}{args_string}' if next is not None else None

        return render_react(
            'SessionDetailsPage',
            'Test Run Session Details',
            close_url=close_url,
            created_at=session_info.created_at,
            session_id=session_info.session_id,
            session_groups=session_info.session_groups,
            session_overview=session_info.session_overview,
            evaluations=session_info.evaluations,
            test_lists=session_info.test_lists,
            previous_url=previous_url,
            next_url=next_url,
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/delete_test_run/<uuid:test_run_id>')
    def delete_test_run(test_run_id: UUID) -> ResponseReturnValue:
        sa.session.execute(delete(TestRun).where(TestRun.id == test_run_id))
        return redirect(f'/projects/{g.project.id}/tests')

    return page
