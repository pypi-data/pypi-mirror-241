from typing import Any, Optional
from dataclasses import dataclass
from uuid import UUID

from flask import Blueprint, g, render_template, request, redirect, abort, url_for, jsonify
from flask.typing import ResponseReturnValue

from freeplay_server.accounts.accounts_blueprint_filters import AccountsBlueprintFilters
from freeplay_server.accounts.accounts_repository import AccountsRepository
from freeplay_server.accounts.user_creator import UserCreator, UserCreationFailure
from freeplay_server.accounts.users import Roles
from freeplay_server.auth.auth_filter import allow_role
from freeplay_server.projects.project_page_blueprint_filters import ProjectPageBlueprintFilters
from freeplay_server.utilities.render_react import render_react
from freeplay_server.web_support import json_support

@dataclass
class CreateUserRequest:
    first_name: str
    last_name: str
    email_address: str
    is_account_admin: bool

@dataclass
class EditUserRequest:
    id: UUID
    first_name: str
    last_name: str
    is_account_admin: bool


def account_show_page(
        filters: AccountsBlueprintFilters,
        project_filters: ProjectPageBlueprintFilters,
        user_creator: UserCreator,
        accounts_repo: AccountsRepository,
) -> Blueprint:
    page = Blueprint('account_show_page', __name__, url_prefix='/settings')

    @page.url_value_preprocessor
    def hydrate_account(_: Optional[str], _values: Optional[dict[str, Any]]) -> None:
        filters.hydrate_account()
        if not hasattr(g, 'account'):
            abort(400)

    @page.url_value_preprocessor
    def hydrate_projects(_: Optional[str], values: Optional[dict[str, Any]]) -> None:
        project_filters.hydrate_projects(values)

    # SINGLE_TENANT
    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/account')
    def show_default_account() -> ResponseReturnValue:
        is_admin_role = g.session_user.is_admin()
        users = accounts_repo.find_all_users_with_role(g.account.id, g.session_user.email_address, is_admin_role)

        return render_react(
            'AccountShowPage',
            title=f'Account {g.account.name}',
            users=users,
            is_admin_role=is_admin_role,
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/accounts')
    def redirect_accounts() -> ResponseReturnValue:
        return redirect(url_for('account_show_page.show_default_account'))

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/accounts/<account_id>')
    def redirect_accounts_detail(account_id: str) -> ResponseReturnValue:
        return redirect(url_for('account_show_page.show_default_account'))

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/account/view_tos')
    def view_tos() -> ResponseReturnValue:
        return render_template('tos_acceptance_modal.html')

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/account/accept_tos')
    def accept_tos() -> ResponseReturnValue:
        accounts_repo.accept_account_tos(g.account.id, g.session_user.email_address)

        return redirect('/')

    @allow_role(Roles.ACCOUNT_ADMIN)
    @page.post('/account/new-user')
    def create_user() -> ResponseReturnValue:
        r = json_support.force_decode(CreateUserRequest, request.data)
        result = user_creator.try_create(g.account.id, r.first_name, r.last_name, r.email_address, r.is_account_admin)

        if type(result) is UserCreationFailure:
            return jsonify({'error_message': result.value}), 400
        return jsonify({'message': 'success'}), 200

    @allow_role(Roles.ACCOUNT_ADMIN)
    @page.post('/account/edit-user')
    def edit_user() -> ResponseReturnValue:
        r = json_support.force_decode(EditUserRequest, request.data)
        result = user_creator.try_edit(r.id, r.first_name, r.last_name, r.is_account_admin)

        if type(result) is UserCreationFailure:
            return jsonify({'error_message': result.value}), 400

        return jsonify({'message': 'success'}), 200

    return page
