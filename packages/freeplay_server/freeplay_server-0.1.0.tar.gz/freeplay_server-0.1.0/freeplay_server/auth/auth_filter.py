import logging
from typing import Callable, Optional, Any, TypeVar

from flask import Flask, request, Response, session, g, redirect, abort
from flask.typing import ResponseReturnValue

from freeplay_server.accounts.accounts_repository import AccountsRepository, DEFAULT_ACCOUNT_NAME
from freeplay_server.accounts.users import Roles, SessionUser
from freeplay_server.auth.api_key_service import ApiKeyService
from freeplay_server.extensions import sa
from freeplay_server.models import AccountUser

logger = logging.getLogger(__name__)


class AuthFilter:
    def __init__(
            self,
            accounts_repo: AccountsRepository,
            app: Flask,
            api_key: str,
            api_key_service: ApiKeyService,
    ):
        self.accounts_repo = accounts_repo
        self.app = app
        self.baked_in_api_key = api_key
        self.api_key_service = api_key_service

    def enforce_auth(self) -> Optional[ResponseReturnValue]:
        # Setup and constraints
        if not request.endpoint:
            abort(404)
        g.account = self.accounts_repo.try_find_by_name(DEFAULT_ACCOUNT_NAME)
        if not g.account:
            raise ValueError("Missing account")

        # Public endpoints
        if request.endpoint == 'static':
            return None  # success
        route = self.app.view_functions[request.endpoint]
        if self.__is_public_endpoint(route):
            return None  # success

        # Check authentication
        if self.__is_api_endpoint(route):
            return self.__require_api_key()
        user = self.__get_session_user()
        if not user:
            return redirect('/login')
        g.session_user = user

        # Check authorization
        return self.__check_authorization(user, self.__allowed_roles(route))

        # Unreachable -- always return from checks.
        abort(500)

    @staticmethod
    def __is_api_endpoint(route: Any) -> bool:
        return getattr(route, 'is_api_endpoint', False)

    @staticmethod
    def __is_public_endpoint(route: Any) -> bool:
        return getattr(route, 'is_public_endpoint', False)

    @staticmethod
    def __allowed_roles(route: Any) -> list[Roles]:
        return getattr(route, 'allowed_roles', [])

    @staticmethod
    def get_current_user() -> Any:
        return g.session_user

    def check_tos_acceptance(self) -> None:
        if hasattr(g, 'session_user') and g.session_user.email_address is not None:
            g.should_accept_tos = self.accounts_repo.should_accept_tos(g.session_user.email_address)

    @staticmethod
    def __get_session_user() -> Optional[SessionUser]:
        user_id = session.get('user_id')
        if not user_id:
            return None
        account_user = sa.session.query(AccountUser).where(AccountUser.user_id == user_id).one_or_none()
        if not account_user:
            return None
        return SessionUser(
            id=user_id,
            email_address=account_user.user.email_address,
            roles=[Roles.from_str(role.name) for role in account_user.roles],
            first_name=account_user.user.first_name,
            last_name=account_user.user.last_name,
        )

    def __require_api_key(self) -> Optional[ResponseReturnValue]:
        if 'Authorization' not in request.headers:
            return Response(status=401)

        auth_header_fields = request.headers['Authorization'].split(maxsplit=1)
        if len(auth_header_fields) != 2:
            return Response('Invalid Authorization header.', status=401)

        request_api_key = auth_header_fields[1]
        if request_api_key == self.baked_in_api_key:
            return None  # success

        if self.api_key_service.matches(account_id=g.account.id, plain_api_key=request_api_key):
            return None  # success
        return Response(status=401)

    @staticmethod
    def __check_authorization(user: SessionUser, allowed_roles: list[Roles]) -> Optional[ResponseReturnValue]:
        # For now, admins do NOT have the User role in the database
        implied_user_roles = user.roles
        if user.is_admin():
            implied_user_roles.append(Roles.ACCOUNT_USER)

        if any(user_role in allowed_roles for user_role in implied_user_roles):
            return None  # success
        return Response(status=401)


T = TypeVar('T', bound=Callable[..., Any])


def allow_role(*roles: Roles) -> Callable[[T], T]:
    for role in roles:
        if not isinstance(role, Roles):
            raise ValueError("Unexpected type for role")

    def decorator(function: T) -> T:
        setattr(function, 'allowed_roles', list(roles))
        return function

    return decorator


def public_endpoint(function: T) -> T:
    setattr(function, 'is_public_endpoint', True)
    return function


def api_endpoint(function: T) -> T:
    setattr(function, 'is_api_endpoint', True)
    return function
