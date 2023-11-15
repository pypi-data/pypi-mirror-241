import statistics
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any
from uuid import UUID

from sqlalchemy import select

from freeplay_server.database_support.database_gateway import DatabaseGateway
from freeplay_server.evaluations.eval_page import EvalCriteriaType
from freeplay_server.extensions import sa
from freeplay_server.models import ProjectSession, TestList, TestRun, EvaluationCriteria, EvaluationResult
from freeplay_server.project_sessions.project_sessions_repository import ProjectSessionsRepository
from freeplay_server.test_lists.test_lists_repository import TestListRecord, TestListsRepository


@dataclass(frozen=True)
class TestRunSubject:
    project_session_id: Optional[UUID]
    inputs: dict[str, str]


@dataclass(frozen=True)
class TestRunWithSubjects:
    id: UUID
    subjects: list[TestRunSubject]


@dataclass
class TestRunListRow:
    id: UUID
    created_at: datetime
    project_id: UUID
    test_list_id: UUID


@dataclass
class TestRunListRecord:
    id: UUID
    created_at: datetime
    project_id: UUID
    test_list_id: UUID


@dataclass(frozen=True)
class MostCommonFirstTemplateVersion:
    prompt_template_version_id: UUID
    created_at: datetime
    model_name: Optional[str]
    name: str
    prompt_template_id: UUID


def map_list_row_to_list_record(row: TestRunListRow) -> TestRunListRecord:
    return TestRunListRecord(
        id=row.id,
        created_at=row.created_at,
        project_id=row.project_id,
        test_list_id=row.test_list_id
    )


class TestRunsService:

    def __init__(
            self,
            db: DatabaseGateway,
            project_sessions_repo: ProjectSessionsRepository,
            test_lists_repo: TestListsRepository):
        self.db = db
        self.project_sessions_repo = project_sessions_repo
        self.test_lists_repo = test_lists_repo

    def find_all_by_project_with_sessions(self, project_id: UUID) -> list[TestRun]:
        return (
            sa.session.query(TestRun)
            # left join to grab test runs without sessions
            .outerjoin(ProjectSession)
            .outerjoin(EvaluationResult)
            .join(TestList)
            .filter(TestList.project_id == project_id)
            .options(sa.orm.joinedload(TestRun.project_sessions))  # Load all ProjectSessions for each TestRun
            .order_by(TestRun.created_at.desc(), ProjectSession.start_time.desc())
        ).all()

    def create(self, test_list: TestListRecord) -> TestRunWithSubjects:
        with self.db.transaction() as connection:
            test_run_id = self.db.create_returning_id(
                sql="""
                    insert into test_runs (test_list_id)
                    values (:test_list_id) returning id
                """,
                connection=connection,
                test_list_id=test_list.id,
            )

            test_cases = self.test_lists_repo.find_test_cases_for_test_list(test_list.id)
            return TestRunWithSubjects(
                id=test_run_id,
                subjects=[TestRunSubject(s.created_from_session_id, s.inputs) for s in test_cases]
            )

    def find_test_run_sessions(self, test_run_id: UUID) -> list[ProjectSession]:
        query = (
            select(ProjectSession)
            .where(ProjectSession.test_run_id == test_run_id)
            .order_by(ProjectSession.start_time.desc())
        )
        return list(sa.session.execute(query).scalars())

    @staticmethod
    def summarize_test_run_evals(
            test_run: TestRun,
            evaluation_criteria: list[EvaluationCriteria]
    ) -> dict[str, str]:
        eval_scores: dict[UUID, list[Any]] = defaultdict(list)

        for session in test_run.project_sessions:
            for result in session.evaluation_results:
                eval_scores[result.evaluation_criteria_id].append(result.score())

        eval_summary_info = {}
        for criteria in evaluation_criteria:
            if criteria.id in eval_scores:
                if criteria.type == EvalCriteriaType.OneToFive:
                    mean = statistics.mean(eval_scores[criteria.id])
                    eval_summary_info[str(criteria.id)] = round(mean, 2)

                elif criteria.type == EvalCriteriaType.YesNo:
                    yes = sum(v == 'yes' for v in eval_scores[criteria.id])
                    no = len(eval_scores[criteria.id]) - yes
                    eval_summary_info[str(criteria.id)] = f'Yes: {yes} | No: {no}'

        return eval_summary_info

    def most_common_first_template_version(self, test_run_id: UUID) -> Optional[MostCommonFirstTemplateVersion]:
        return self.db.try_find(
            type=MostCommonFirstTemplateVersion,
            sql="""
            SELECT prompt_template_version_id, pt.name, ptv.created_at, pt.id as prompt_template_id, model_name, COUNT(*) AS occurrences
            FROM (
              SELECT
                pse.prompt_template_version_id AS prompt_template_version_id,
                lm.name AS model_name,
                ROW_NUMBER() OVER (PARTITION BY pse.project_session_id ORDER BY pse.logged_at) AS rn
              FROM test_runs
                JOIN project_sessions ON project_sessions.test_run_id = test_runs.id
                JOIN project_session_entries AS pse ON pse.project_session_id = project_sessions.id
                JOIN llm_models AS lm on pse.model_id = lm.id
              WHERE test_runs.id = :test_run_id
            ) t
            JOIN prompt_template_versions as ptv ON ptv.id = t.prompt_template_version_id
            JOIN prompt_templates as pt ON pt.id = ptv.prompt_template_id
            WHERE t.rn = 1
            GROUP BY prompt_template_version_id, pt.name, ptv.created_at, pt.id, model_name
            ORDER BY occurrences DESC
            LIMIT 1;
            """,
            test_run_id=test_run_id,
        )
