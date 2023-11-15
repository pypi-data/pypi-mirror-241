from uuid import UUID

from freeplay_server.projects.test_builders import build_test_project_record
from freeplay_server.test_lists.test_lists_repository import TestListRecord, TestListFields

default_project_id = build_test_project_record().id


def build_test_list_fields(name: str = 'Good ones', description: str = 'Good') -> TestListFields:
    return TestListFields(
        name=name,
        description=description,
    )


def build_test_list_record(
        id: UUID = UUID(hex='f1a8b59b-a5e7-4415-9c0b-7f8d11fffe78'),
        project_id: UUID = default_project_id,
        name: str = build_test_list_fields().name,
        description: str = 'description') -> TestListRecord:
    return TestListRecord(
        id=id,
        project_id=project_id,
        name=name,
        description=description,
    )
