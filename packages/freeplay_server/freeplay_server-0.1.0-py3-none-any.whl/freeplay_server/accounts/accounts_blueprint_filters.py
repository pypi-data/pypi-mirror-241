from typing import Optional, Callable
from uuid import UUID

from flask import g

from freeplay_server.accounts.accounts_repository import AccountRecord, AccountsRepository

AccountFinder = Callable[[UUID], Optional[AccountRecord]]


class AccountsBlueprintFilters:
    def __init__(self, accounts_repo: AccountsRepository):
        self.accounts_repo = accounts_repo

    def hydrate_account(self) -> None:
        g.account = self.accounts_repo.try_find_by_name('Default Account')
