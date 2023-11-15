from dataclasses import dataclass
from enum import Enum
from typing import Union, List, Optional
from uuid import UUID
from datetime import datetime

from sqlalchemy.exc import IntegrityError

from freeplay_server.database_support.database_gateway import DatabaseGateway


@dataclass(frozen=True)
class ApiKeyRecord:
    name: str
    key_hash: str
    last: str
    account_id: UUID
    created_by: UUID
    created_at: Optional[datetime]
    created_by_user_email: Optional[str]


class ApiKeyPersistenceFailure(Enum):
    NameAlreadyTaken = 'A key with this name already exists'
    InvalidUserOrAccount = 'An invalid user ID was given'
    InvalidKeyName = 'The key name given does not exist'
    NameEmpty = 'The name cannot be empty'


class ApiKeysRepository:

    def __init__(self, db: DatabaseGateway):
        self.db = db

    def find_all(self, account_id: UUID) -> List[ApiKeyRecord]:
        return self.db.find_all(
            type=ApiKeyRecord,
            sql="select name, key_hash, last, account_id, created_by, created_at, users.email_address as created_by_user_email "
                "from api_keys join users on users.id=api_keys.created_by "
                "where account_id = :account_id "
                "order by name",
            account_id=account_id
        )

    def find_with_last(self, account_id: UUID, last: str) -> List[ApiKeyRecord]:
        return self.db.find_all(
            type=ApiKeyRecord,
            sql="select name, key_hash, last, account_id, created_by "
                "from api_keys "
                "where account_id = :account_id and last = :last ",
            account_id=account_id,
            last=last
        )

    def find_with_name(self, account_id: UUID, name: str) -> List[ApiKeyRecord]:
        return self.db.find_all(
            type=ApiKeyRecord,
            sql="select name, key_hash, last, account_id, created_by "
                "from api_keys "
                "where account_id = :account_id and name = :name ",
            account_id=account_id,
            name=name
        )

    def persist_api_key(
            self,
            name: str,
            api_key_hash: str,
            last: str,
            account_id: UUID,
            created_by: UUID
    ) -> Union[ApiKeyRecord, ApiKeyPersistenceFailure]:
        with self.db.transaction() as connection:
            name_exists = self.db.exists(
                'select count(name) '
                'from api_keys '
                'where name = :name and account_id = :account_id',
                connection,
                name=name,
                account_id=account_id
            )
            if name == '':
                return ApiKeyPersistenceFailure.NameEmpty

            if name_exists:
                return ApiKeyPersistenceFailure.NameAlreadyTaken

            try:
                return self.db.create(
                    ApiKeyRecord,
                    """
                    insert into api_keys (name, key_hash, last, account_id, created_by) 
                    values (:name, :key_hash, :last, :account_id, :created_by)
                    returning *
                    """,
                    connection,
                    name=name,
                    key_hash=api_key_hash,
                    last=last,
                    account_id=account_id,
                    created_by=created_by,
                )
            except IntegrityError as e:
                return ApiKeyPersistenceFailure.InvalidUserOrAccount

    def delete(self, account_id: UUID, name: str) -> Union[int, ApiKeyPersistenceFailure]:
        rows_deleted = self.db.execute_return_count(
            sql='delete from api_keys '
                'where account_id = :account_id and name = :name',
            account_id=account_id,
            name=name)
        if rows_deleted == 0:
            return ApiKeyPersistenceFailure.InvalidKeyName
        return rows_deleted
