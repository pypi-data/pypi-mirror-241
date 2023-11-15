import logging
from enum import Enum
from typing import Union, cast, Optional
from uuid import UUID

import stytch
from stytch.core.models import StytchError

from freeplay_server.accounts.accounts_repository import UserPersistenceFailure, UserRecord, AccountsRepository

logger = logging.getLogger(__name__)


class UserCreationFailure(Enum):
    ErrorCreatingMember = 'There was an error creating the Member with Stytch'
    AccountNotFound = 'Could not find account'
    NameAlreadyTaken = 'This email is already taken'
    NameEmpty = 'The name cannot be empty'
    NameTooLong = 'The name cannot be longer than 200 characters'


class UserCreator:

    def __init__(self, repo: AccountsRepository, stytch_client: stytch.Client):
        self.repo = repo
        self.stytch_client = stytch_client

    def try_create(self,
                   account_id: UUID,
                   first_name: str,
                   last_name: str,
                   email_address: str,
                   is_admin_user: bool = False,
                   ) -> Union[UserRecord, UserCreationFailure]:
        if email_address == '' or first_name == '' or last_name == '':
            return UserCreationFailure.NameEmpty

        if len(email_address) > 200 or len(first_name) > 200 or len(last_name) > 200:
            return UserCreationFailure.NameTooLong

        account = self.repo.try_find(account_id)
        if account is None:
            return UserCreationFailure.AccountNotFound

        if self.repo.find_user_by_email_address(email_address):
            return UserCreationFailure.NameAlreadyTaken

        try:
            response = self.stytch_client.users.create(email=email_address)
        except StytchError as e:
            return UserCreationFailure.ErrorCreatingMember

        persistence_result = self.repo.create_user(
            first_name,
            last_name,
            email_address,
            account_id,
            response.user_id,
            is_admin_user=is_admin_user
        )
        if type(persistence_result) is UserPersistenceFailure:
            return UserCreationFailure.NameAlreadyTaken

        try:
            _response = self.stytch_client.magic_links.email.login_or_create(email_address)
        except StytchError as e:
            logger.error("Could not send invite email: %s", e)

        return cast(UserRecord, persistence_result)

    def try_edit(self,
                 user_id: UUID,
                 first_name: str,
                 last_name: str,
                 is_admin_user: bool,
                 ) -> Optional[UserCreationFailure]:
        if first_name == '' or last_name == '':
            return UserCreationFailure.NameEmpty

        if len(first_name) > 200 or len(last_name) > 200:
            return UserCreationFailure.NameTooLong

        persistence_result = self.repo.edit_user(
            user_id,
            first_name,
            last_name,
            is_admin_user=is_admin_user
        )
        if type(persistence_result) is UserPersistenceFailure:
            return UserCreationFailure.NameAlreadyTaken

        return None
