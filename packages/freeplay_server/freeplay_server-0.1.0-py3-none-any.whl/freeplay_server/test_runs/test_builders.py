from typing import Optional
from uuid import UUID

from freeplay_server.project_sessions.test_builders import build_test_project_session, default_test_run_id
from freeplay_server.test_runs.test_runs_service import TestRunWithSubjects, TestRunSubject


def build_test_test_run_subject(
    project_session_id: UUID = build_test_project_session().session_id,
    inputs: Optional[dict[str, str]] = None,
) -> TestRunSubject:
    inputs = inputs or {'question': 'What can you tell me about flamingos?'}

    return TestRunSubject(project_session_id, inputs)


def build_test_test_run(
    id: UUID = default_test_run_id,
    subjects: Optional[list[TestRunSubject]] = None
) -> TestRunWithSubjects:
    subjects = subjects or [build_test_test_run_subject()]

    return TestRunWithSubjects(id, subjects)
