from dataclasses import dataclass
from typing import Optional, cast, Any
from uuid import UUID

from flask import Blueprint, g, jsonify
from flask.typing import ResponseReturnValue

from freeplay_server.auth.auth_filter import api_endpoint
from freeplay_server.projects.project_page_blueprint_filters import ProjectPageBlueprintFilters
from freeplay_server.projects.projects_repository import ProjectRecord
from freeplay_server.prompt_templates.llm_model_parameters import LLMModelParameterValue
from freeplay_server.prompt_templates.prompt_template_version_repository import PromptTemplateVersionRepository, \
    PromptTemplateVersion


@dataclass
class PromptTemplate:
    project_version_id: UUID  # we can maybe use this field but use the prompt_template_version_id
    prompt_template_version_id: UUID
    prompt_template_id: UUID
    name: str
    content: str
    flavor_name: Optional[str]
    params: Optional[dict[str, Any]] = None


def prompt_templates_api(
        filters: ProjectPageBlueprintFilters,
        prompt_template_version_repo: PromptTemplateVersionRepository
) -> Blueprint:
    api = Blueprint('prompt_templates_api', __name__, url_prefix='/api/projects/<project_id>/templates')

    @api.url_value_preprocessor
    def hydrate_projects(_: Optional[str], values: Optional[dict[str, Any]]) -> None:
        filters.hydrate_projects(values)

    @api.before_request
    def before_request() -> Optional[ResponseReturnValue]:
        return filters.before_api_request()

    @api_endpoint
    @api.get('/all/<tag>')
    def all_by_tag(tag: str) -> ResponseReturnValue:
        project = cast(ProjectRecord, g.project)

        templates = prompt_template_version_repo.find_all_templates_by_project_id_and_tag(project.id, tag)
        hydrated_templates = __render_templates(templates)

        return_val = {
            "templates": hydrated_templates
        }

        return jsonify(return_val), 200

    def __render_templates(
            templates: list[PromptTemplateVersion]
    ) -> list[PromptTemplate]:
        hydrated_templates = []
        for template_version in templates:
            structured_params: dict[str, LLMModelParameterValue] = {}
            if template_version.api_version:
                structured_params['api_version'] = template_version.api_version
            if template_version.deployment_id:
                structured_params['deployment_id'] = template_version.deployment_id
            if template_version.resource_name:
                structured_params['resource_name'] = template_version.resource_name
            if template_version.prompt_template_config:
                structured_params['model'] = template_version.prompt_template_config.model_name
                for param in template_version.prompt_template_config.parameters:
                    structured_params[param.name] = param.value

            hydrated_templates.append(PromptTemplate(
                # Note: this field actually represents the prompt_template_version_id -- the value is correct but
                # the field remains for backwards compatibility. TODO: ENG-547
                project_version_id=template_version.id,
                prompt_template_version_id=template_version.id,
                prompt_template_id=template_version.prompt_template_id,
                name=template_version.name,
                content=template_version.content,
                flavor_name=template_version.prompt_template_config.flavor_name if template_version.prompt_template_config else None,
                params=structured_params if bool(structured_params) else None
            ))

        return hydrated_templates

    return api
