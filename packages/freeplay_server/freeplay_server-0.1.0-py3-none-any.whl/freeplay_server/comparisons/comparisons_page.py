from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any, Tuple
from urllib.parse import urlparse
from uuid import UUID

from flask import abort, g, Blueprint, redirect, render_template, request, url_for, current_app
from flask.typing import ResponseReturnValue
from sqlalchemy.exc import NoResultFound

from freeplay_server.accounts.users import Roles
from freeplay_server.auth.auth_filter import allow_role
from freeplay_server.comparisons.comparisons import ComparisonType
from freeplay_server.comparisons.comparisons_service import ComparableSession, ComparableSessionType, Template
from freeplay_server.comparisons.comparisons_service import ComparisonsService, ComparisonPreferredResult
from freeplay_server.extensions import sa
from freeplay_server.models import Comparison, TestCaseComparison, TestCase, Environment
from freeplay_server.models import TestRun
from freeplay_server.project_sessions.prompt_model import PromptModel
from freeplay_server.projects.project_page_blueprint_filters import ProjectPageBlueprintFilters
from freeplay_server.prompt_templates.llm_model_parameters import LLMModelParameterValue
from freeplay_server.prompt_templates.prompt_template_version_repository import PromptTemplateVersion, LATEST_TAG_NAME
from freeplay_server.prompt_templates.prompt_templates_page import PromptTemplateConfigShowParameter
from freeplay_server.test_lists.test_lists_page import TestListInfo
from freeplay_server.test_runs.test_runs_service import TestRunsService, MostCommonFirstTemplateVersion
from freeplay_server.utilities.render_react import render_react


def get_result_for_test_case_comparison(
        comparison_type: ComparisonType,
        comparison: TestCaseComparison,
        test_runs: list[TestRun]
) -> Tuple[str, Optional[float], str, str]:
    result_timestamp = None
    if not comparison.is_scored:
        result = ''
        preferred_result = ''
        badge_style = ''
    elif comparison_type == ComparisonType.Vs_Original and comparison.preferred_test_run_id:
        test_run = next(test_run for test_run in test_runs if test_run.id == comparison.preferred_test_run_id)
        result = f'Test Run'
        result_timestamp = test_run.created_at.timestamp()
        preferred_result = ComparisonPreferredResult.Right
        badge_style = 'green'
    elif comparison_type == ComparisonType.Vs_Original and comparison.is_scored and not comparison.preferred_test_run_id and comparison.preferred_original:
        result = test_runs[0].test_list.name
        preferred_result = ComparisonPreferredResult.Left
        badge_style = 'blue'
    elif comparison_type == ComparisonType.Vs_Test_Runs and comparison.is_scored and comparison.preferred_test_run_id:
        (index, test_run) = next((index, test_run) for (index, test_run) in enumerate(test_runs) if
                                 test_run.id == comparison.preferred_test_run_id)
        result = f'Test Run'
        result_timestamp = test_run.created_at.timestamp()
        badge_style = 'blue' if index == 0 else 'green'
        preferred_result = ComparisonPreferredResult.Left if index == 0 else ComparisonPreferredResult.Right
    elif comparison.is_scored:
        result = 'Neutral'
        preferred_result = ComparisonPreferredResult.Neutral
        badge_style = 'yellow'
    else:
        raise Exception("Unexpected preferred result ID")

    return result, result_timestamp, preferred_result, badge_style


@dataclass
class TestCaseInfo:
    inputs: dict[str, str]
    result: str
    result_timestamp: Optional[float]
    badge_style: str

    def __init__(self, comparison: TestCaseComparison, project_id: UUID, comparison_id: UUID, test_case_id: UUID,
                 inputs: dict[str, str], test_runs: list[TestRun], comparison_type: ComparisonType):
        (result, result_timestamp, preferred_result, badge_style) = get_result_for_test_case_comparison(
            comparison_type,
            comparison,
            test_runs)
        self.inputs = inputs
        self.result = result
        self.result_timestamp = result_timestamp
        self.preferred_result = preferred_result
        self.badge_style = badge_style
        self.comparison_url = f'/projects/{project_id}/comparisons/{comparison_id}/test_cases/{test_case_id}'


@dataclass
class ComparisonInfo:
    id: UUID
    num_test_cases: int
    not_scored_test_cases_count: int
    prefer_right_count: int
    prefer_left_count: int
    tied_count: int
    created_at: int
    left_name: str
    left_timestamp: Optional[float]
    right_name: str
    right_timestamp: float
    left_model: Optional[str] = None
    right_model: Optional[str] = None

    def __init__(
            self,
            comparison: Comparison,
            prompts: Optional[list[Optional[MostCommonFirstTemplateVersion]]] = None
    ) -> None:
        self.id = comparison.id
        results = [
            get_result_for_test_case_comparison(comparison.comparison_type, case, comparison.test_runs) for case
            in comparison.test_case_comparisons]

        self.num_test_cases = len(comparison.test_case_comparisons)
        self.not_scored_test_cases_count = sum(1 for (_, _, preferred_result, _) in results if preferred_result == '')
        self.prefer_right_count = sum(
            1 for (_, _, preferred_result, _) in results if preferred_result == ComparisonPreferredResult.Right)
        self.prefer_left_count = sum(
            1 for (_, _, preferred_result, _) in results if preferred_result == ComparisonPreferredResult.Left)
        self.tied_count = sum(
            1 for (_, _, preferred_result, _) in results if preferred_result == ComparisonPreferredResult.Neutral)

        if comparison.comparison_type == ComparisonType.Vs_Original:
            self.left_name = comparison.first_test_run().test_list.name
            self.left_timestamp = None
            self.left_model = None
            self.right_name = f'Test Run'
            self.right_timestamp = comparison.first_test_run().created_at.timestamp()
            if prompts and len(prompts):
                self.right_model = prompts[0].model_name if prompts[0] else None
        elif comparison.comparison_type == ComparisonType.Vs_Test_Runs:
            self.left_name = f'Test Run'
            self.left_timestamp = comparison.first_test_run().created_at.timestamp()
            if prompts and len(prompts):
                self.left_model = prompts[0].model_name if prompts[0] else None
            self.right_name = f'Test Run'
            self.right_timestamp = comparison.test_runs[1].created_at.timestamp()
            if prompts and len(prompts) > 1:
                self.right_model = prompts[1].model_name if prompts[1] else None

        self.created_at = int(comparison.created_at.timestamp())


@dataclass
class PromptForComparisonInfo:
    content: PromptModel
    model_name: Optional[str]
    created_at: int
    name: str
    params: list[PromptTemplateConfigShowParameter]

    def __init__(self, prompt_template_version: PromptTemplateVersion):
        self.content = PromptModel.from_string(prompt_template_version.content)
        self.created_at = int(prompt_template_version.created_at.timestamp())
        self.name = prompt_template_version.name
        if prompt_template_version.prompt_template_config:
            self.model_name = prompt_template_version.prompt_template_config.model_name
            self.params = [PromptTemplateConfigShowParameter(record) for record in
                           prompt_template_version.prompt_template_config.parameters]
        else:
            self.model_name = None
            self.params = []


@dataclass
class DeployPromptInfo:
    prompt_name: str
    created_at: int
    model_name: Optional[str]

    def __init__(self, template: Template, project_id: UUID):
        self.prompt_name = template.name
        self.model_name = template.model_name
        self.created_at = int(template.created_at.timestamp())
        self.version_url = f'/projects/{project_id}/templates/{template.id}/versions/{template.version_id}'


@dataclass
class ParamForComparison:
    name: str
    param_values: list[Optional[LLMModelParameterValue]]


def build_params_for_comparison(prompts: list[Optional[PromptTemplateVersion]]) -> list[ParamForComparison]:
    # Build parameter comparison list
    param_names = set()
    for prompt in prompts:
        if prompt and prompt.prompt_template_config:
            for param in prompt.prompt_template_config.parameters:
                param_names.add(param.name)

    compared_params = []
    for name in param_names:
        params = []
        for prompt in prompts:
            if prompt and prompt.prompt_template_config:
                matching_param = next((p for p in prompt.prompt_template_config.parameters if p.name == name), None)
            else:
                matching_param = None

            params.append(matching_param.value if matching_param else None)

        compared_params.append(ParamForComparison(name, params))
    return compared_params


@dataclass
class ComparisonListInfo:
    detail_url: str
    created_at: int
    status: str
    prompt_name: str
    prompt_version_timestamp: int
    test_list_info: TestListInfo

    def __init__(self, project_id: UUID, comparison: Comparison, prompt_name: str,
                 prompt_version_timestamp: datetime, test_list_info: TestListInfo):
        self.detail_url = f'/projects/{project_id}/comparisons/{comparison.id}'
        self.created_at = int(comparison.created_at.timestamp())
        self.status = comparison.status
        self.cases_evaluated = len(
            [case_cmp for case_cmp in comparison.test_case_comparisons if case_cmp.is_scored])
        self.total_cases = len(comparison.test_case_comparisons)
        self.prompt_name = prompt_name
        self.prompt_version_timestamp = int(prompt_version_timestamp.timestamp())
        self.test_list_info = test_list_info


@dataclass
class ComparableSessionInfo:
    type: ComparableSessionType
    session_id: Optional[UUID]
    response: Optional[str]
    prompt: Optional[PromptForComparisonInfo]
    test_run_id: Optional[UUID]


@dataclass
class CompareSessionsInfo:
    test_list_session_inputs: dict[str, str]
    comparable_sessions: list[ComparableSessionInfo]
    comparable_params: list[ParamForComparison]

    def __init__(
            self,
            test_list_session_inputs: dict[str, str],
            comparable_sessions: list[ComparableSession]
    ) -> None:
        self.test_list_session_inputs = test_list_session_inputs
        self.comparable_sessions = [ComparableSessionInfo(
            session.type,
            session.session_id,
            session.response,
            PromptForComparisonInfo(session.prompt) if session.prompt else None,
            test_run_id=session.test_run_id
        ) for session in comparable_sessions]
        self.comparable_params = build_params_for_comparison([session.prompt for session in comparable_sessions])


def comparisons_page(
        filters: ProjectPageBlueprintFilters,
        comparisons_service: ComparisonsService,
        test_runs_service: TestRunsService
) -> Blueprint:
    page = Blueprint('comparisons_page', __name__, url_prefix='/projects/<project_id>/comparisons')

    @page.url_value_preprocessor
    def hydrate_projects(_: Optional[str], values: Optional[dict[str, Any]]) -> None:
        filters.hydrate_projects(values)

    @page.before_request
    def before_request() -> Optional[ResponseReturnValue]:
        return filters.before_page_request()

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('')
    def show_index() -> ResponseReturnValue:
        comparisons = comparisons_service.get_comparisons_for_project(g.project.id)

        comparison_infos = []
        for comparison in comparisons:
            template_version = comparisons_service.most_common_first_template_version(comparison.id)
            if len(comparison.test_runs) > 0:
                test_run = comparison.first_test_run()
            else:
                raise RuntimeError(f"Comparison id: {comparison.id} missing test run. Failing request.")

            if template_version is not None:
                comparison_infos.append(
                    ComparisonListInfo(g.project.id, comparison, template_version.name, template_version.created_at,
                                       TestListInfo(test_run.test_list)))

        return render_template(
            'comparisons_list.html',
            comparisons=comparison_infos,
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/<uuid:test_run_id>')
    @page.post('/<uuid:test_run_id>/<uuid:target>')
    def create_comparison(test_run_id: UUID, target: Optional[UUID] = None) -> ResponseReturnValue:
        all_test_runs = [test_run_id]
        if target:
            all_test_runs.append(target)

        comparison = comparisons_service.create_comparison(test_run_id, all_test_runs)
        return redirect(f'/projects/{g.project.id}/comparisons/{comparison.id}')

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/<uuid:comparison_id>')
    def show_comparison_details(comparison_id: UUID) -> ResponseReturnValue:
        comparison = sa.session.query(Comparison).where(Comparison.id == comparison_id).one_or_none()
        if not comparison:
            abort(404)

        test_case_infos = [TestCaseInfo(case, g.project.id, comparison.id, case.test_case_id, case.test_case.inputs,
                                        comparison.test_runs, comparison.comparison_type) for case in
                           comparison.test_case_comparisons]

        prompts = [test_runs_service.most_common_first_template_version(test_run.id) for test_run in
                   comparison.test_runs]

        comparison_info = ComparisonInfo(comparison, prompts)

        return render_template(
            'comparison_details.html',
            test_list_name=comparison.first_test_run().test_list.name,
            test_case_infos=test_case_infos,
            comparison_info=comparison_info,
            finish_comparison_url=f'/projects/{g.project.id}/comparisons/{comparison.id}/finish',
            test_list_url=f'/projects/{g.project.id}/test_lists/{comparison.first_test_run().test_list.id}',
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/<uuid:comparison_id>/finish')
    def finish_comparison(comparison_id: UUID) -> ResponseReturnValue:
        action = request.form.get('action')
        if action == 'end':
            comparisons_service.finish_comparison(comparison_id)

            return redirect(f'/projects/{g.project.id}/comparisons/{comparison_id}')
        elif action == 'deploy':
            return redirect(f'/projects/{g.project.id}/comparisons/{comparison_id}/deploy')
        else:
            raise Exception(f"Unexpected action: {action}")

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/<uuid:comparison_id>/deploy')
    def show_deploy_page(comparison_id: UUID) -> ResponseReturnValue:
        comparison = sa.session.query(Comparison).where(Comparison.id == comparison_id).one_or_none()
        if not comparison or not comparison.first_test_run().id:
            abort(404)

        tags = [environment.name for environment in sa.session.query(Environment).where(
            Environment.is_deleted == False
        ).where(Environment.name != LATEST_TAG_NAME).all()]

        templates = comparisons_service.get_templates_to_deploy_for_comparison(comparison.id)
        template_infos = [DeployPromptInfo(template, g.project.id) for template in templates]

        return render_template(
            'comparison_deploy.html',
            comparison_url=f'/projects/{g.project.id}/comparisons/{comparison.id}',
            deploy_url=f'/projects/{g.project.id}/comparisons/{comparison.id}/deploy',
            templates=template_infos,
            tags=tags,
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/<uuid:comparison_id>/deploy')
    def deploy_comparison(comparison_id: UUID) -> ResponseReturnValue:
        tags = list(request.form.keys())
        try:
            comparisons_service.deploy_comparison(comparison_id, tags)
        except NoResultFound:
            abort(404)

        return redirect(f'/projects/{g.project.id}')

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/<uuid:comparison_id>/test_cases/<uuid:test_case_id>')
    def set_comparison_for_test_case(comparison_id: UUID, test_case_id: UUID) -> ResponseReturnValue:
        preferred_result = request.args.get('preferred_result')

        comparison = sa.session.query(Comparison).where(Comparison.id == comparison_id).one_or_none()
        if not comparison:
            abort(404)

        ordered_comparison_set = comparisons_service.get_sibling_test_case_comparisons(
            comparison.test_case_comparisons, test_case_id)

        # Mutating db state to set preferred result
        comparisons_service.update_preferred_result_for_test_case_comparison(
            ordered_comparison_set.test_case, preferred_result)

        next_test_case = ordered_comparison_set.next_test_case

        return redirect(url_for('comparisons_page.compare_test_run_results',
                                comparison_id=comparison_id,
                                project_id=g.project.id,
                                test_case_id=next_test_case.test_case_id) if next_test_case else url_for(
            'comparisons_page.show_comparison_details', project_id=g.project.id, comparison_id=comparison_id))

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/<uuid:comparison_id>/test_cases/<uuid:test_case_id>')
    def compare_test_run_results(comparison_id: UUID, test_case_id: UUID) -> ResponseReturnValue:
        try:
            comparison = sa.session.query(Comparison).where(Comparison.id == comparison_id).one()

            (test_case_comparison, test_case) = sa.session.query(
                TestCaseComparison,
                TestCase
            ).join(TestCaseComparison.test_case).filter(
                TestCaseComparison.comparison_id == comparison.id
            ).filter(TestCase.id == test_case_id).one()
        except NoResultFound:
            abort(404)

        ordered_comparison_set = comparisons_service.get_sibling_test_case_comparisons(
            comparison.test_case_comparisons, test_case_id)

        comparable_sessions = comparisons_service.view_comparison(comparison, test_case)
        comparison_info = ComparisonInfo(comparison)

        # If we're navigating from another case comparison, don't animate the footer. If we're navigating here from the
        # dashboard, animate the footer.
        animate_footer = __referrer_endpoint() != request.endpoint

        return render_react(
            'CompareTestRunResultsPage',
            title=f'Comparing test case {ordered_comparison_set.display_index} of {len(comparison.test_case_comparisons)}',
            hide_main_nav=True,
            compare_sessions_info=CompareSessionsInfo(
                test_list_session_inputs=test_case_comparison.test_case.inputs,
                comparable_sessions=comparable_sessions
            ),
            close_url=f'/projects/{g.project.id}/comparisons/{comparison.id}',
            previous_test_case_id=ordered_comparison_set.previous_test_case.test_case_id if ordered_comparison_set.previous_test_case else None,
            next_test_case_id=ordered_comparison_set.next_test_case.test_case_id if ordered_comparison_set.next_test_case else None,
            test_case_index=ordered_comparison_set.display_index,
            animate_footer=animate_footer,
            comparison_info=comparison_info,
            test_case_id=test_case_comparison.test_case_id,
        )

    def __referrer_endpoint() -> Optional[str]:
        referrer = request.headers.get('Referer')
        if referrer:
            try:
                referrer_path = urlparse(referrer).path
                adapter = current_app.url_map.bind('')
                return adapter.match(referrer_path, method='GET')[0]
            except Exception:
                return None
        else:
            return None

    return page
