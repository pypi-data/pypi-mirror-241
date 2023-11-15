import json
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Union, Optional
from uuid import UUID

from sqlalchemy import Connection
from sqlalchemy.orm import joinedload

from freeplay_server.database_support.database_gateway import DatabaseGateway
from freeplay_server.extensions import sa
from freeplay_server.models import TestList
from freeplay_server.project_sessions.project_sessions_repository import ProjectSessionDetailsRecord, \
    ProjectSessionsRecord


@dataclass(frozen=True)
class TestListFields:
    name: str
    description: Optional[str]


@dataclass(frozen=True)
class TestListRecord:
    id: UUID
    project_id: UUID
    name: str
    description: Optional[str]
    input_keys: Optional[list[str]] = None
    deleted_at: Optional[datetime] = None


@dataclass(frozen=True)
class TestCaseRecord:
    id: UUID
    inputs: dict[str, str]
    created_from_session_id: Optional[UUID]
    uploaded_output: Optional[str]


class TestListPersistenceFailure(Enum):
    NameAlreadyTaken = 'This name is already taken'
    NameEmpty = 'The name cannot be empty'
    NameTooLong = 'The name cannot be longer than 100 characters'


@dataclass
class TestCaseUpload:
    inputs: dict[str, str]
    output: Optional[str]


class TestListsRepository:

    def __init__(self, db: DatabaseGateway):
        self.db = db

    def try_find_by_project_id_and_name(self, project_id: UUID, test_list_name: str) -> Optional[TestListRecord]:
        return self.db.try_find(
            type=TestListRecord,
            sql="""
                select test_lists.* from test_lists
                where test_lists.project_id = :project_id
                    and test_lists.name = :test_list_name
                    and test_lists.deleted_at is null
            """,
            project_id=project_id,
            test_list_name=test_list_name,
        )

    def try_find(self, test_list_id: UUID) -> Optional[TestListRecord]:
        return self.db.try_find(
            type=TestListRecord,
            sql="""
                select test_lists.* from test_lists
                where test_lists.id = :test_list_id
            """,
            test_list_id=test_list_id,
        )

    def find_all_by_project_id(self, project_id: UUID, include_deleted: bool = False) -> list[TestList]:
        test_lists_query = sa.session.query(TestList).where(
            TestList.project_id == project_id
        ).options(joinedload(TestList.test_cases)).order_by(TestList.name.asc())

        if include_deleted:
            return test_lists_query.all()
        else:
            return test_lists_query.filter(TestList.deleted_at.is_(None)).all()

    def find_all_by_session_id(self, session_id: UUID) -> list[TestListRecord]:
        return self.db.find_all(
            type=TestListRecord,
            sql="""
                select
                    test_lists.id,
                    test_lists.project_id,
                    test_lists.name,
                    test_lists.description
                from test_lists
                join test_list_test_cases on test_lists.id = test_list_test_cases.test_list_id
                join test_cases on test_list_test_cases.test_case_id = test_cases.id
                where test_cases.created_from_session_id = :session_id
                    and test_lists.deleted_at is null
            """,
            session_id=session_id,
        )

    def create(
            self,
            project_id: UUID,
            fields: TestListFields,
    ) -> Union[TestListPersistenceFailure, TestListRecord]:
        field_validation_error = self.__validate_test_list_fields(fields)
        if field_validation_error:
            return field_validation_error

        with self.db.transaction() as connection:
            name_already_taken = self.db.exists(
                sql='select count(1) from test_lists where project_id=:project_id and name=:name',
                connection=connection,
                project_id=project_id,
                name=fields.name,
            )

            if name_already_taken:
                return TestListPersistenceFailure.NameAlreadyTaken

            test_list = self.db.create(
                type=TestListRecord,
                sql="""
                    insert into test_lists (project_id, name, description) 
                    values (:project_id, :name, :description)
                    returning *
                """,
                connection=connection,
                project_id=project_id,
                name=fields.name,
                description=fields.description,
            )

            return test_list

    def update(
            self,
            project_id: UUID,
            test_list_id: UUID,
            fields: TestListFields,
    ) -> Optional[TestListPersistenceFailure]:
        field_validation_error = self.__validate_test_list_fields(fields)
        if field_validation_error:
            return field_validation_error

        with self.db.transaction() as connection:
            name_already_taken = self.db.exists(
                sql='select count(1) from test_lists where project_id=:project_id and name=:name and test_lists.id <> :test_list_id',
                connection=connection,
                project_id=project_id,
                name=fields.name,
                test_list_id=test_list_id
            )

            if name_already_taken:
                return TestListPersistenceFailure.NameAlreadyTaken

            self.db.update(
                type=TestListRecord,
                sql="""
                    update test_lists
                    SET  name= :name, description=:description
                    WHERE id = :test_list_id AND project_id = :project_id
                    returning test_lists.*
                """,
                connection=connection,
                name=fields.name,
                description=fields.description,
                test_list_id=test_list_id,
                project_id=project_id
            )
            return None

    def soft_delete_test_list(self, test_list_id: UUID) -> None:
        return self.db.execute(
            sql="""
            UPDATE test_lists 
            SET deleted_at=now()
            WHERE id = :test_list_id
            """,
            test_list_id=test_list_id
        )

    def delete_test_case_from_test_list(self, test_list_id: UUID, test_case_id: UUID) -> None:
        return self.db.execute(
            sql='DELETE FROM test_list_test_cases WHERE test_case_id = :test_case_id AND test_list_id=:test_list_id',
            test_case_id=test_case_id,
            test_list_id=test_list_id,
        )

    def find_test_cases_for_test_list(self, test_list_id: UUID) -> list[TestCaseRecord]:
        test_case_records = self.db.find_all(
            type=TestCaseRecord,
            sql="""
            SELECT 
                id, 
                inputs, 
                created_from_session_id, 
                uploaded_output
            FROM
                test_cases
            JOIN
                test_list_test_cases ON test_list_test_cases.test_case_id = test_cases.id
            WHERE
                test_list_id = :test_list_id
            ORDER BY
                test_list_test_cases.created_at DESC
            """,
            test_list_id=test_list_id,
        )

        return test_case_records

    def update_session_test_lists(self, session: ProjectSessionDetailsRecord, test_list_ids: list[UUID]) -> None:
        with self.db.transaction() as connection:
            for test_list_id in test_list_ids:
                test_list = self.try_find(test_list_id)
                if not test_list:
                    raise RuntimeError('Test list not found')
                if test_list.input_keys is None:
                    self.__set_input_keys_for_empty_test_list(
                        connection=connection,
                        test_list_id=test_list_id,
                        input_keys=list(session.entries[0].inputs.keys()),
                    )
                elif set(test_list.input_keys) != set(session.entries[0].inputs.keys()):
                    raise Exception('Input keys do not match')

            test_case_id = self.__insert_test_case_if_not_exists(
                connection=connection,
                inputs=json.dumps(session.entries[0].inputs),
                session_id=session.id,
            )

            self.__add_test_case_to_test_lists(connection, test_case_id, test_list_ids)
            self.__remove_session_from_test_cases(connection, test_list_ids, test_case_id)

    def add_sessions_to_test_list(self, test_list_id: UUID, sessions: list[ProjectSessionsRecord]) -> None:
        if not sessions:
            return
        with self.db.transaction() as connection:
            test_list = self.try_find(test_list_id)
            if not test_list:
                raise RuntimeError('Test list not found')
            test_list_input_keys = test_list.input_keys
            if test_list_input_keys is None:
                test_list_input_keys = list(sessions[0].inputs.keys())
                self.__set_input_keys_for_empty_test_list(
                    connection=connection,
                    test_list_id=test_list_id,
                    input_keys=test_list_input_keys,
                )
            test_case_ids = []
            for session in sessions:
                if set(test_list_input_keys) != set(session.inputs.keys()):
                    raise Exception('Input keys do not match')
                test_case_id = self.__insert_test_case_if_not_exists(
                    connection=connection,
                    inputs=json.dumps(session.inputs),
                    session_id=session.id,
                )
                test_case_ids.append(test_case_id)

            self.__add_test_cases_to_test_list(connection, test_case_ids, test_list_id)

    def insert_uploaded_test_cases(self, test_list_id: UUID, test_case_uploads: list[TestCaseUpload]) -> None:
        if not test_case_uploads:
            return
        input_keys = set(test_case_uploads[0].inputs.keys())
        for tc in test_case_uploads:
            if set(tc.inputs.keys()) != input_keys:
                raise Exception('Input keys do not match')

        with self.db.transaction() as connection:
            test_list = self.try_find(test_list_id)
            if not test_list:
                raise Exception('Test list not found')

            if test_list.input_keys is None:
                self.__set_input_keys_for_empty_test_list(
                    connection=connection,
                    test_list_id=test_list_id,
                    input_keys=list(input_keys),
                )
            elif set(test_list.input_keys) != input_keys:
                raise Exception('Input keys do not match')

            for tc in test_case_uploads:
                self.db.execute(
                    sql="""
                        WITH new_test_case AS (
                            INSERT INTO test_cases (inputs, uploaded_output)
                            VALUES (:inputs, :uploaded_output)
                            RETURNING id
                        )
                        INSERT INTO test_list_test_cases (test_case_id, test_list_id)
                        SELECT id, :test_list_id FROM new_test_case
                    """,
                    connection=connection,
                    inputs=json.dumps(tc.inputs),
                    uploaded_output=tc.output,
                    test_list_id=test_list_id,
                )

    def __remove_session_from_test_cases(
            self, connection: Connection, test_list_ids: list[UUID], test_case_id: UUID) -> None:
        if len(test_list_ids) > 0:
            self.db.execute(
                sql="""
                    DELETE FROM test_list_test_cases
                    WHERE test_list_id not in :test_list_ids
                        AND test_case_id = :test_case_id
                """,
                connection=connection,
                test_list_ids=tuple(test_list_ids),
                test_case_id=test_case_id
            )
        else:
            self.db.execute(
                sql="""
                    DELETE FROM test_list_test_cases WHERE test_case_id = :test_case_id
                """,
                connection=connection,
                test_case_id=test_case_id
            )

    def __insert_test_case_if_not_exists(self, connection: Connection, inputs: str,
                                         session_id: UUID) -> UUID:
        test_case = self.db.try_find(
            type=TestCaseRecord,
            sql="""
                SELECT * FROM test_cases WHERE created_from_session_id = :session_id
            """,
            connection=connection,
            session_id=session_id,
        )
        if test_case is not None:
            return test_case.id

        return self.db.create_returning_id(
            sql="""
                                INSERT INTO test_cases (inputs, created_from_session_id)
                                VALUES (:inputs, :created_from_session_id)
                                RETURNING ID
                            """,
            connection=connection,
            inputs=inputs,
            created_from_session_id=session_id,
        )

    def __add_test_case_to_test_lists(self, connection: Connection, test_case_id: UUID,
                                      test_list_ids: list[UUID]) -> None:
        if not test_list_ids:
            return None
        self.db.insert_multi(
            sql="""
            insert into test_list_test_cases (test_list_id, test_case_id)
            values (:test_list_id, :test_case_id)
            on conflict do nothing
            """,
            connection=connection,
            values=[{'test_case_id': test_case_id, 'test_list_id': test_list_id} for test_list_id in test_list_ids],
        )

    def __add_test_cases_to_test_list(self, connection: Connection, test_case_ids: list[UUID],
                                      test_list_id: UUID) -> None:
        if not test_case_ids:
            return None
        self.db.insert_multi(
            sql="""
            insert into test_list_test_cases (test_list_id, test_case_id)
            values (:test_list_id, :test_case_id)
            on conflict do nothing
            """,
            connection=connection,
            values=[{'test_case_id': test_case_id, 'test_list_id': test_list_id} for test_case_id in test_case_ids],
        )

    def __set_input_keys_for_empty_test_list(self, connection: Connection, test_list_id: UUID,
                                             input_keys: list[str]) -> None:
        self.db.execute(
            sql="""
                update test_lists
                set input_keys = :input_keys
                where id = :id
            """,
            connection=connection,
            id=test_list_id,
            input_keys=input_keys,
        )

    def get_compatible_test_lists(self, project_id: UUID, input_keys: list[str]) -> list[TestListRecord]:
        return self.db.find_all(
            type=TestListRecord,
            sql="""
                SELECT *
                FROM test_lists
                WHERE ((input_keys @> :input_keys AND input_keys <@ :input_keys) OR input_keys IS NULL)
                AND project_id = :project_id
                AND deleted_at is NULL
            """,
            input_keys=input_keys,
            project_id=project_id,
        )

    @staticmethod
    def __validate_test_list_fields(fields: TestListFields) -> Optional[TestListPersistenceFailure]:
        if fields.name == '':
            return TestListPersistenceFailure.NameEmpty

        if len(fields.name) > 100:
            return TestListPersistenceFailure.NameTooLong
        return None
