import uuid
from enum import Enum
from typing import Union, cast

from freeplay_server.database_support.database_gateway import DatabaseGateway
from freeplay_server.projects.projects_repository import ProjectRecord, ProjectPersistenceFailure


class ProjectCreationFailure(Enum):
    NameAlreadyTaken = 'This name is already taken'
    NameEmpty = 'The name cannot be empty'
    NameTooLong = 'The name cannot be longer than 100 characters'


ProjectCreationResult = Union[
    ProjectRecord,
    ProjectPersistenceFailure,
]


class ProjectCreator:

    def __init__(self, db: DatabaseGateway):
        self.db = db

    def try_create(self, name: str) -> Union[ProjectRecord, ProjectCreationFailure]:
        if name == '':
            return ProjectCreationFailure.NameEmpty

        if len(name) > 100:
            return ProjectCreationFailure.NameTooLong

        persistence_result = self.__create_project(name)
        if type(persistence_result) is ProjectPersistenceFailure:
            return ProjectCreationFailure.NameAlreadyTaken

        return cast(ProjectRecord, persistence_result)

    def __create_project(self, name: str) -> ProjectCreationResult:
        with self.db.transaction() as connection:
            name_exists = self.db.exists(
                'select count(id) from projects where name = :name',
                connection,
                name=name,
            )

            if name_exists:
                return ProjectPersistenceFailure.NameAlreadyTaken

            new_id = uuid.uuid4()
            project_id = self.db.create_returning_id("""
                            insert into projects (id, name) 
                            values (:project_id, :name) returning id
                            """, connection, project_id=new_id, name=name)
            return ProjectRecord(project_id, name)
