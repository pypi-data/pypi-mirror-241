import logging
import time
from dataclasses import dataclass
from enum import Enum
from typing import Union, cast
from uuid import UUID, uuid4

import argon2

from freeplay_server.auth.api_keys_repository import ApiKeysRepository, ApiKeyPersistenceFailure

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class NewApiKey:
    name: str
    api_key: UUID
    last: str


@dataclass(frozen=True)
class PersistedKey:
    name: str
    last: str


class ApiKeyCreationFailure(Enum):
    NameAlreadyTaken = 'This API key name is already taken'
    InvalidUserOrAccount = 'An invalid user ID or account ID was given'
    NameEmpty = 'The name cannot be empty'


ApiKeyCreationResult = Union[
    NewApiKey,
    ApiKeyCreationFailure,
]


class ApiKeyService:
    # Memory: 2**15 kibibytes is approximately 33 MiB
    # Memory: 2**16 kibibytes is approximately 67 MiB
    # Memory: 2**17 kibibytes is approximately 133 MiB

    # These parameters are critical to the security of the hash.
    # See: https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
    __argon2Hasher = argon2.PasswordHasher(
        time_cost=3, memory_cost=2 ** 15, parallelism=1, hash_len=32, salt_len=16)

    def __init__(
            self,
            key_repo: ApiKeysRepository
    ):
        self.api_keys_repo = key_repo

    def create_key(
            self,
            name: str,
            account_id: UUID,
            created_by: UUID
    ) -> ApiKeyCreationResult:
        # It is important that this UUID generation be cryptographically secure. In this case, it means
        # the underlying random number generator used be cryptographically secure. Python's uuid4 should
        # be such an implementation, but be careful if you change something here.
        # See: https://stackoverflow.com/a/53542384
        new_key = uuid4()

        persist_result = self.persist_api_key(
            account_id=account_id,
            created_by=created_by,
            name=name,
            plain_key=str(new_key))

        if type(persist_result) is ApiKeyCreationFailure:
            return persist_result

        persisted_key = cast(PersistedKey, persist_result)

        return NewApiKey(
            name=name,
            api_key=new_key,
            last=persisted_key.last)

    def persist_api_key(
            self,
            name: str,
            account_id: UUID,
            created_by: UUID,
            plain_key: str
    ) -> Union[PersistedKey, ApiKeyCreationFailure]:
        hashed = ApiKeyService.hash_key(str(plain_key))
        last_four = str(plain_key)[-4:]

        persist_result = self.api_keys_repo.persist_api_key(
            name=name,
            api_key_hash=hashed,
            last=last_four,
            account_id=account_id,
            created_by=created_by)

        if persist_result is ApiKeyPersistenceFailure.NameEmpty:
            return ApiKeyCreationFailure.NameEmpty
        if persist_result is ApiKeyPersistenceFailure.NameAlreadyTaken:
            return ApiKeyCreationFailure.NameAlreadyTaken
        if persist_result is ApiKeyPersistenceFailure.InvalidUserOrAccount:
            return ApiKeyCreationFailure.InvalidUserOrAccount

        return PersistedKey(name=name, last=last_four)

    def matches(self, account_id: UUID, plain_api_key: str) -> bool:
        # This _should_ only ever return one row. It should be safe, albeit slower, if it somehow returns
        # multiple because of a collision on the last 4
        for api_key_record in self.api_keys_repo.find_with_last(account_id=account_id, last=plain_api_key[-4:]):
            if self.__argon2Hasher.verify(api_key_record.key_hash, plain_api_key):
                return True
        return False

    @classmethod
    def hash_key(cls, plain: str) -> str:
        start = time.time()
        hashed = cls.__argon2Hasher.hash(str(plain))
        end = time.time()
        logger.info("Time to hash key: %.3fs" % (end - start))
        return hashed
