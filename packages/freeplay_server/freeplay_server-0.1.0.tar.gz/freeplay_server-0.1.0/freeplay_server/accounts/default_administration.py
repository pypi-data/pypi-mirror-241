import logging
from typing import cast, Optional
from uuid import UUID

import stytch
from stytch.core.models import StytchError, SearchQuery, Operand

from freeplay_server.accounts.accounts_repository import AccountsRepository, AccountPersistenceFailure, AccountRecord, \
    UserRecord, UserPersistenceFailure, DEFAULT_ACCOUNT_NAME
from freeplay_server.auth.api_key_service import ApiKeyService, ApiKeyCreationFailure

logger = logging.getLogger(__name__)


class DefaultAdministration:
    def __init__(
            self,
            api_key_service: ApiKeyService,
            accounts_repo: AccountsRepository,
            stytch_client: stytch.Client
    ):
        self.api_key_service = api_key_service
        self.accounts_repo = accounts_repo
        self.stytch_client = stytch_client

    def provision(self, email_address: str, is_internal_user: bool = False, is_admin_user: bool = False) -> bool:
        admin_account = self.__ensure_default_account()
        if admin_account is None:
            return False

        admin_user = self.__create_default_user(admin_account.id, email_address, is_internal_user, is_admin_user)
        return admin_user is not None

    def ensure_default_api_key(self, default_email_address: str, api_key: str) -> bool:
        default_account = self.__ensure_default_account()
        if not default_account:
            logger.warning("Could not find default account to ensure the default API key exists.")
            return False

        api_key_exists = self.api_key_service.matches(
            account_id=default_account.id,
            plain_api_key=api_key)

        if not api_key_exists:
            user = self.accounts_repo.find_user_by_email_address(default_email_address)
            if not user:
                logger.warning("Could not find user to store default API key.")
                return False

            persist_api_key = self.api_key_service.persist_api_key(
                "default_api_key",
                default_account.id,
                user.id,
                api_key)

            if isinstance(persist_api_key, ApiKeyCreationFailure):
                logger.warning("Could not store default API key: %s" % persist_api_key)
                return False

        return True

    def __ensure_default_account(self) -> Optional[AccountRecord]:
        default_account_name = 'Default Account'
        maybe_default_account = self.accounts_repo.try_find_by_name(default_account_name)

        if maybe_default_account is not None:
            logger.debug('Default account exists, no account creation necessary')
            return maybe_default_account

        create_result = self.accounts_repo.create_account(DEFAULT_ACCOUNT_NAME)
        if type(create_result) is AccountPersistenceFailure:
            logger.error('Unable to create default account. Cause: %s' % create_result)
            return None

        logger.debug('Default account created')
        return cast(AccountRecord, create_result)

    def __create_default_user(self, account_id: UUID, email_address: str, is_internal: bool, is_admin_user: bool) -> Optional[UserRecord]:
        existing_user = self.accounts_repo.find_user_by_email_address(email_address)
        if existing_user is not None:
            logger.debug('User %s already exists, so skipping default user creation', email_address)
            return None

        stytch_user_id = self.__ensure_stytch_user(email_address)
        if stytch_user_id is None:
            logger.error('Unable to create default user %s in stytch', email_address)
            return None

        create_result = self.accounts_repo.create_user(
            'Default',
            'User',
            email_address,
            account_id,
            stytch_user_id,
            is_internal,
            is_admin_user)
        if type(create_result) is UserPersistenceFailure:
            logger.error('Unable to create default user user')
            return None

        logger.debug('Default user %s created', email_address)
        return cast(UserRecord, create_result)

    def __ensure_stytch_user(self, email_address: str) -> Optional[str]:
        try:
            create_response = self.stytch_client.users.create(email=email_address)
            logger.debug('User %s created in Stytch', email_address)
            return cast(str, create_response.user_id)
        except StytchError as e:
            if e.details.error_type != 'duplicate_email':
                logger.error('Unable to create default user in stytch %s', e)
                return None

        try:
            search_results = self.stytch_client.users.search(
                query=SearchQuery(operator='AND',
                                  operands=[Operand(filter_name='email_address', filter_value=[email_address])])
            ).results
        except StytchError as e:
            logger.error('Unable to retrieve default user from stytch %s', e)
            return None

        if len(search_results) != 1:
            logger.error('Found %d stytch users with email %s', len(search_results), email_address)
            return None

        logger.debug('User %s found in Stytch', email_address)
        return cast(str, search_results[0].user_id)
