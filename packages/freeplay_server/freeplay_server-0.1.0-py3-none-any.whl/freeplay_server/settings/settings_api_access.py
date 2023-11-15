from typing import Optional, Any
from uuid import UUID

from flask import Blueprint, render_template, request, g, abort, jsonify
from flask.typing import ResponseReturnValue

from freeplay_server.accounts.accounts_blueprint_filters import AccountsBlueprintFilters
from freeplay_server.accounts.users import Roles
from freeplay_server.auth.api_key_service import ApiKeyService, ApiKeyCreationFailure
from freeplay_server.auth.api_keys_repository import ApiKeysRepository
from freeplay_server.auth.auth_filter import allow_role
from freeplay_server.projects.project_page_blueprint_filters import ProjectPageBlueprintFilters


def api_access_show_page(
        filters: AccountsBlueprintFilters,
        project_filters: ProjectPageBlueprintFilters,
        api_key_service: ApiKeyService,
        api_key_repo: ApiKeysRepository,
) -> Blueprint:
    page = Blueprint('api_access_show_page', __name__, url_prefix='/settings/api-access')

    @page.url_value_preprocessor
    def hydrate_account(_: Optional[str], _values: Optional[dict[str, Any]]) -> None:
        filters.hydrate_account()
        if not hasattr(g, 'account'):
            abort(400)

    @page.url_value_preprocessor
    def hydrate_projects(_: Optional[str], values: Optional[dict[str, Any]]) -> None:
        project_filters.hydrate_projects(values)

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('')
    def show_api_keys() -> ResponseReturnValue:
        all_account_api_keys = api_key_repo.find_all(g.account.id)
        return render_template(
            'api_access_list.html',
            all_account_api_keys=all_account_api_keys
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/new-api-key')
    def request_new_api_key() -> ResponseReturnValue:
        return render_template(
            'new_api_key_modal.html',
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/new-api-key')
    def create_new_api_key() -> ResponseReturnValue:
        name = request.form['name']
        result = api_key_service.create_key(name=name, account_id=g.account.id, created_by=g.session_user.id)

        if isinstance(result, ApiKeyCreationFailure):
            return render_template(
                'new_api_key_modal.html',
                error_message=result.value
            ), 200

        # Success case
        return render_template(
            'show_newly_created_api_key_modal.html',
            api_key=result.api_key,
            key_name=result.name,
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/request_deletion/<api_key_last_arg>')
    def request_deletion(api_key_last_arg: UUID) -> ResponseReturnValue:
        return render_template(
            'api_access_deletion_confirmation_modal.html',
            api_key_last=api_key_last_arg,
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.delete('/<api_key_last_arg>')
    def delete_api_key(api_key_last_arg: str) -> ResponseReturnValue:
        api_key_details = api_key_repo.find_with_last(g.account.id, last=api_key_last_arg)
        if api_key_details is None:
            return jsonify({'error': 'Not Found'}), 404

        api_key_repo.delete(g.account.id, api_key_details[0].name)
        return jsonify({})

    return page
