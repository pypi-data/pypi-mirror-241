from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Optional
from uuid import UUID

from freeplay_server.comparisons.comparisons import ComparisonType
from freeplay_server.database_support.database_gateway import DatabaseGateway
from freeplay_server.extensions import sa
from freeplay_server.models import Comparison, TestRun, TestCaseComparison, ProjectSession, TestCase, TestList, \
    test_run_comparison
from freeplay_server.project_sessions.project_sessions_repository import ProjectSessionsRepository
from freeplay_server.prompt_templates.prompt_template_version_repository import PromptTemplateVersionRepository, \
    PromptTemplateVersion
from freeplay_server.test_lists.test_lists_repository import TestListsRepository


class ComparisonPreferredResult(StrEnum):
    Left = 'left'  # left is the original session or uploaded output
    Right = 'right'  # right is the output from the test run
    Neutral = 'neutral'


@dataclass(frozen=True)
class CaseComparisonRecord:
    id: UUID
    comparison_id: UUID
    test_case_id: UUID
    created_at: datetime
    session_id: Optional[UUID]
    inputs: dict[str, str]
    preferred_result: Optional[ComparisonPreferredResult]


class ComparisonStatus(StrEnum):
    Deployed = 'Deployed'
    Ended = 'Ended'
    NeedsReview = 'Needs Review'


@dataclass(frozen=True)
class MostCommonFirstTemplateVersion:
    ptv_id: UUID
    created_at: datetime
    name: str


@dataclass(frozen=True)
class Template:
    name: str
    version_id: UUID
    id: UUID
    created_at: datetime
    model_name: Optional[str]


@dataclass
class OrderedComparisonSet:
    display_index: int
    test_case: TestCaseComparison
    previous_test_case: Optional[TestCaseComparison]
    next_test_case: Optional[TestCaseComparison]


# StrEnum should *not* be a data class or else it cannot safely be serialized to a value in JSON.
class ComparableSessionType(StrEnum):
    Original = 'original'
    TestRunSession = 'test_run_session'


@dataclass
class ComparableSession:
    type: ComparableSessionType
    session_id: Optional[UUID]
    response: Optional[str]
    ptv_id: Optional[UUID]
    prompt: Optional[PromptTemplateVersion]
    test_run_id: Optional[UUID]


class ComparisonsService:

    def __init__(
            self,
            db: DatabaseGateway,
            test_lists_repo: TestListsRepository,
            project_sessions_repo: ProjectSessionsRepository,
            prompt_template_version_repo: PromptTemplateVersionRepository
    ):
        self.db = db
        self.test_lists_repo = test_lists_repo
        self.project_sessions_repo = project_sessions_repo
        self.prompt_template_version_repo = prompt_template_version_repo

    def create_comparison(
            self,
            base_test_run_id: UUID,
            all_test_run_ids: list[UUID]
    ) -> Comparison:
        if len(all_test_run_ids) > 1:
            comparison_type = ComparisonType.Vs_Test_Runs
        else:
            comparison_type = ComparisonType.Vs_Original
        base_test_run = sa.session.query(TestRun).where(TestRun.id == base_test_run_id).one()

        all_test_runs = sa.session.query(TestRun).where(
            TestRun.id.in_(all_test_run_ids)
        ).all()

        comparison = Comparison(
            comparison_type=comparison_type,
            status=ComparisonStatus.NeedsReview,
            test_runs=all_test_runs
        )

        # Add and flush to get a relational ID.
        sa.session.add(comparison)
        sa.session.flush()

        for i, test_case in enumerate(base_test_run.test_list.test_cases):
            test_case_comparison = TestCaseComparison(
                comparison_id=comparison.id,
                test_case_id=test_case.id,
                sort_order=i)
            sa.session.add(test_case_comparison)

        sa.session.commit()

        return comparison

    def get_comparisons_for_project(self, project_id: UUID) -> list[Comparison]:
        # Need to join to test_list to get to a table with project_id.
        return sa.session.query(Comparison).join(test_run_comparison).join(TestRun).join(TestList).filter(
            TestList.project_id == project_id
        ).order_by(Comparison.created_at.desc()).all()

    def update_preferred_result_for_test_case_comparison(
            self,
            test_case_comparison: TestCaseComparison,
            preferred_result: Optional[str]
    ) -> None:
        test_case_comparison.is_scored = True
        if preferred_result == 'ORIGINAL':
            test_case_comparison.preferred_test_run_id = None
            test_case_comparison.preferred_original = True
        elif preferred_result:
            test_case_comparison.preferred_test_run_id = UUID(preferred_result)
            test_case_comparison.preferred_original = False
        else:
            test_case_comparison.preferred_test_run_id = None
            test_case_comparison.preferred_original = None

        sa.session.commit()

    def finish_comparison(self, comparison_id: UUID) -> None:
        comparison = sa.session.query(Comparison).where(Comparison.id == comparison_id).one()
        comparison.status = ComparisonStatus.Ended
        sa.session.commit()

    def get_templates_to_deploy_for_comparison(self, comparison_id: UUID) -> list[Template]:
        comparison = sa.session.query(Comparison).where(Comparison.id == comparison_id).one()

        if not comparison.test_runs[0].id:
            raise RuntimeError("Comparison did not contain test_run_id. Cannot deploy.")

        if comparison.comparison_type == ComparisonType.Vs_Original:
            # Vs. Original, deploy the only test run
            test_run_id = comparison.test_runs[0].id
        else:
            # Vs. another test run, deploy the preferred test run.
            test_run_id = self.__find_preferred_test_run_id(comparison.test_case_comparisons) or comparison.first_test_run().id

        return self.__all_templates_for_test_run(test_run_id)

    def deploy_comparison(self, comparison_id: UUID, tags: list[str]) -> None:
        comparison = sa.session.query(Comparison).where(Comparison.id == comparison_id).one()

        for template in self.get_templates_to_deploy_for_comparison(comparison.id):

            self.prompt_template_version_repo.update_template_tags(
                template.version_id, template.id, tags, connection=sa.session.connection())

        comparison.status = ComparisonStatus.Deployed
        sa.session.commit()

    def get_sibling_test_case_comparisons(
            self,
            test_case_comparisons: list[TestCaseComparison],
            test_case_id: UUID
    ) -> OrderedComparisonSet:
        previous_case = None
        next_case = None
        test_case = None
        display_index = 0

        for i, element in enumerate(test_case_comparisons):
            if element.test_case_id == test_case_id:
                previous_case = test_case_comparisons[i - 1] if i > 0 else None
                next_case = test_case_comparisons[i + 1] if i < len(test_case_comparisons) - 1 else None
                display_index = i + 1
                test_case = element
                break

        if not test_case:
            raise RuntimeError(f"Did not find test case id {test_case_id} in comparison.")

        return OrderedComparisonSet(display_index, test_case, previous_case, next_case)

    def view_comparison(self, comparison: Comparison, test_case: TestCase) -> list[ComparableSession]:
        comparable_session_info = []
        # If comparing to original, include in results.
        if comparison.comparison_type == ComparisonType.Vs_Original:
            comparable_session_info.append(self.__original_session_info_for_test_case(test_case))

        for test_run in comparison.test_runs:
            comparable_session_info.append(self.__find_session_for_test_run_test_case(test_case, test_run))

        return self.__hydrate_template_versions_for_sessions(comparable_session_info)

    def __find_preferred_test_run_id(self, test_case_comparisons: list[TestCaseComparison]) -> Optional[UUID]:
        preferred_test_run_counts: dict[UUID, int] = {}
        for test_case_comparison in test_case_comparisons:
            preferred_test_run_id = test_case_comparison.preferred_test_run_id
            if preferred_test_run_id in preferred_test_run_counts:
                preferred_test_run_counts[preferred_test_run_id] += 1
            elif preferred_test_run_id:
                preferred_test_run_counts[preferred_test_run_id] = 1

        try:
            preferred_test_run_count = max(preferred_test_run_counts.items(), key=lambda tuple: tuple[1])
            return preferred_test_run_count[0]
        except ValueError:
            return None


    def __original_session_info_for_test_case(self, test_case: TestCase) -> ComparableSession:
        return ComparableSession(
            ComparableSessionType.Original,
            test_case.created_from_session_id,
            test_case.uploaded_output or test_case.created_from_session.last_response() if test_case.created_from_session else None,
            test_case.created_from_session.entries[
                0].prompt_template_version_id if test_case.created_from_session else None,
            None, None)

    def __hydrate_template_versions_for_sessions(
            self,
            comparable_session_info: list[ComparableSession]
    ) -> list[ComparableSession]:
        test_run_ptv_ids = []
        for comp_session_info in comparable_session_info:
            if comp_session_info.ptv_id:
                test_run_ptv_ids.append(comp_session_info.ptv_id)

        # Hydrate all prompt_template_versions
        test_run_ptvs = self.prompt_template_version_repo.find_template_version_by_ids(
            test_run_ptv_ids, sa.session.connection())

        # Fill in prompt template versions into comparison info.
        for comp_session_info in comparable_session_info:
            if comp_session_info.ptv_id:
                comp_session_info.prompt = test_run_ptvs[comp_session_info.ptv_id]
        return comparable_session_info

    def __find_session_for_test_run_test_case(
            self,
            test_case: TestCase,
            test_run: TestRun
    ) -> ComparableSession:
        all_test_run_sessions = sa.session.query(ProjectSession).where(
            ProjectSession.test_run_id == test_run.id).all()
        session = next(
            (session for session in all_test_run_sessions if session.first_inputs() == test_case.inputs), None)
        if session:
            ptv_id = session.entries[0].prompt_template_version_id
            return ComparableSession(
                ComparableSessionType.TestRunSession, session.id, session.last_response(), ptv_id, None, test_run.id)
        else:
            return ComparableSession(
                ComparableSessionType.TestRunSession, None, None, None, None, test_run.id
            )

    def most_common_first_template_version(self, comparison_id: UUID) -> Optional[MostCommonFirstTemplateVersion]:
        # Goal: Find the prompt template version that the test run was most intentionally trying to test.
        # This is done by finding the most common first template version used in the test run.
        return self.db.try_find(
            type=MostCommonFirstTemplateVersion,
            sql="""
            SELECT ptv_id, pt.name, ptv.created_at, COUNT(*) AS occurrences
            FROM (
              SELECT
                pse.prompt_template_version_id AS ptv_id,
                ROW_NUMBER() OVER (PARTITION BY pse.project_session_id ORDER BY pse.logged_at) AS rn
              FROM comparisons
                JOIN comparison_test_runs ON comparisons.id = comparison_test_runs.comparison_id
                JOIN project_sessions ON project_sessions.test_run_id = comparison_test_runs.test_run_id
                JOIN project_session_entries AS pse ON pse.project_session_id = project_sessions.id
              WHERE comparisons.id = :comparison_id
            ) t
            JOIN prompt_template_versions as ptv ON ptv.id = t.ptv_id
            JOIN prompt_templates as pt ON pt.id = ptv.prompt_template_id
            WHERE t.rn = 1
            GROUP BY ptv_id, pt.name, ptv.created_at
            ORDER BY occurrences DESC
            LIMIT 1;
            """,
            comparison_id=comparison_id,
            connection=sa.session.connection()
        )

    def __all_templates_for_test_run(self, test_run_id: UUID) -> list[Template]:
        return self.db.find_all(
            type=Template,
            sql="""
            select distinct pt.name, pt.id, ptv.id as version_id, ptv.created_at, lm.name as model_name
            from test_runs
            join project_sessions as ps on ps.test_run_id = test_runs.id
            join project_session_entries as pse on pse.project_session_id = ps.id
            join prompt_template_versions as ptv on ptv.id = pse.prompt_template_version_id
            join prompt_templates as pt on pt.id = ptv.prompt_template_id
            left join prompt_template_model_configs on ptv.model_config_id = prompt_template_model_configs.id
            left join llm_models as lm on prompt_template_model_configs.model_id = lm.id
            where test_runs.id = :test_run_id
            """,
            test_run_id=test_run_id,
            connection=sa.session.connection()
        )
