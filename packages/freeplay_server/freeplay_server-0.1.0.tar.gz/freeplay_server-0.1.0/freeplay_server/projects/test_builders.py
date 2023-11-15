from uuid import UUID

from freeplay_server.projects.projects_repository import ProjectRecord


def build_test_project_record(
        id: UUID = UUID(hex='09902a19-7705-4f4a-8bb5-34cebefd831f'),
        name: str = 'My Project'
) -> ProjectRecord:
    return ProjectRecord(id=id, name=name)
