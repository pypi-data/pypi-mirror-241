from enum import Enum
from dataclasses import dataclass
from uuid import UUID
from typing import Union, cast

from freeplay_server.database_support.database_gateway import DatabaseGateway
from freeplay_server.settings.settings_repository import EnvironmentType


@dataclass
class Environment:
    id: UUID
    name: str

class EnvironmentCreationFailure(Enum):
    NameAlreadyTaken = 'This name is already taken'
    NameEmpty = 'The name cannot be empty'
    NameTooLong = 'The name cannot be longer than 100 characters'

EnvironmentCreationResult = Union[
    EnvironmentType,
    Environment,
    EnvironmentCreationFailure
]

class EnvironmentCreator:

    def __init__(self, db: DatabaseGateway):
        self.db = db

    def try_create(self, name: str) -> EnvironmentCreationResult:
        if name == '':
            return EnvironmentCreationFailure.NameEmpty

        if len(name) > 100:
            return EnvironmentCreationFailure.NameTooLong

        persistence_result = self.__create_environment(name)
        if type(persistence_result) is EnvironmentCreationFailure:
            return EnvironmentCreationFailure.NameAlreadyTaken

        return cast(EnvironmentType, persistence_result)

    def __create_environment(self, name: str) -> EnvironmentCreationResult:
        with self.db.transaction() as connection:
            name_exists = self.db.exists(
                'SELECT COUNT(id) FROM environments WHERE name = :name',
                connection,
                name=name,
            )

            if name_exists:
                return EnvironmentCreationFailure.NameAlreadyTaken

            environment_id = self.db.create_returning_id(
                sql="""
                    INSERT INTO environments (name)
                    VALUES (:name) returning id
                """,
                connection=connection,
                name=name
            )

            return Environment(environment_id, name)
