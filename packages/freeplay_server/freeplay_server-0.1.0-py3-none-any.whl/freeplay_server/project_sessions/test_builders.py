from uuid import UUID

from freeplay_server.project_sessions.project_session_creator import ProjectSession

default_test_run_id: UUID = UUID(hex='7d040757-bb04-45f6-a2b4-6520a518ecf7')


def build_test_project_session(
        session_id: UUID = UUID(hex='cb129c2e-9a29-477d-b6fe-f359bee72101'),
) -> ProjectSession:
    return ProjectSession(session_id=session_id)
