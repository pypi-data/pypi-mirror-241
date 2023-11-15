from enum import Enum
from typing import Union, cast

from freeplay_server.accounts.accounts_repository import AccountPersistenceFailure, AccountRecord, AccountsRepository


class AccountCreationFailure(Enum):
    NameAlreadyTaken = 'This name is already taken'
    NameEmpty = 'The name cannot be empty'
    NameTooLong = 'The name cannot be longer than 100 characters'
    ErrorCreatingOrganization = 'There was an error creating the Organization with Stytch'


class AccountCreator:

    def __init__(self, repo: AccountsRepository):
        self.repo = repo

    def try_create(self, name: str) -> Union[AccountRecord, AccountCreationFailure]:
        if name == '':
            return AccountCreationFailure.NameEmpty

        if len(name) > 100:
            return AccountCreationFailure.NameTooLong

        persistence_result = self.repo.create_account(name)
        if type(persistence_result) is AccountPersistenceFailure:
            return AccountCreationFailure.NameAlreadyTaken

        return cast(AccountRecord, persistence_result)
