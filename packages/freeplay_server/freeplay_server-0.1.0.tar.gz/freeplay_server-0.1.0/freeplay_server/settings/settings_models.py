from typing import Any, Optional, List
from uuid import UUID

from flask import Blueprint, request, jsonify, g
from flask.typing import ResponseReturnValue

from freeplay_server.accounts.users import Roles
from freeplay_server.auth.auth_filter import allow_role
from freeplay_server.projects.project_page_blueprint_filters import ProjectPageBlueprintFilters
from freeplay_server.settings.settings_repository import (
    ModelsRepository,
    ModelsType,
    AzureEndpointType,
    AzureNewEndpointType
)
from freeplay_server.utilities.render_react import render_react


def models_show_page(
        filters: ProjectPageBlueprintFilters,
        models_repo: ModelsRepository,
) -> Blueprint:
    page = Blueprint('models_show_page', __name__, url_prefix='/settings/models')

    @page.url_value_preprocessor
    def hydrate_projects(_: Optional[str], values: Optional[dict[str, Any]]) -> None:
        filters.hydrate_projects(values)

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('')
    def show_models() -> ResponseReturnValue:
        default_models = models_repo.find_default_models()
        models: List[ModelsType] = []

        for model in default_models:
            flavor_type = ''
            if model.name == 'openai_chat':
                flavor_type = 'Chat (default)'
            elif model.name == 'openai_text':
                flavor_type = 'Text (legacy)'

            models.append(ModelsType(
                id=model.id,
                display_name=model.display_name,
                name=model.name,
                is_active=model.is_active,
                provider_name=model.provider_name,
                flavor_type=flavor_type,
                is_default=model.is_default,
            ))

        azure_models = models_repo.find_non_default_models(filter_by_provider=('azure',))
        azure_endpoints = models_repo.find_all_azure_endpoints(g.account.id)
        return render_react(
            'ModelsPage',
            title='Models',
            default_models=models,
            azure_models=azure_models,
            endpoint_model_configs=azure_endpoints,
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('')
    def update_models() -> ResponseReturnValue:
        request_data = request.get_json()
        for model in request_data.get('default', []):
            models_repo.update_models(ModelsType(**model))

        for model in request_data.get('azure'):
            if model.get('id'):
                models_repo.update_azure_endpoint(AzureEndpointType(**model), g.account.id)
            else:
                models_repo.create_azure_endpoint(AzureNewEndpointType(**model), g.account.id)

        return jsonify({})

    @allow_role(Roles.ACCOUNT_USER)
    @page.delete('/<uuid:endpoint_id>')
    def delete_endpoint(endpoint_id: UUID) -> ResponseReturnValue:
        models_repo.delete_endpoint(endpoint_id, g.account.id)

        return jsonify({})

    return page
