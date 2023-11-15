import logging
from dataclasses import dataclass
from typing import Optional, Any
from uuid import UUID

from flask import Blueprint, jsonify, render_template, g
from flask.typing import ResponseReturnValue

from freeplay_server.accounts.users import Roles
from freeplay_server.auth.auth_filter import allow_role
from freeplay_server.projects.project_page_blueprint_filters import ProjectPageBlueprintFilters
from freeplay_server.prompt_templates.llm_model_repository import LLMModelRepository, \
    LLMModelParametersRecord
from freeplay_server.prompt_templates.prompt_template_version_repository import PromptTemplateVersion
from freeplay_server.prompt_templates.prompt_template_version_repository import PromptTemplateVersionRepository
from freeplay_server.prompt_templates.prompt_templates_page import AllowedModelConfigShowFields, EnvironmentInfo
from freeplay_server.settings.settings_repository import EnvironmentsRepository
from freeplay_server.utilities.render_react import render_react

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class PromptListShowFields:
    prompt_template_id: UUID
    name: str
    last_updated_at: int
    model_name: Optional[str] = None
    llm_parameters: Optional[LLMModelParametersRecord] = None


def prompt_templates_list_page(
        filters: ProjectPageBlueprintFilters,
        prompt_template_version_repo: PromptTemplateVersionRepository,
        llm_model_repository: LLMModelRepository,
        environments_repo: EnvironmentsRepository) -> Blueprint:
    page = Blueprint('prompt_templates_list_page', __name__, url_prefix='/projects/<project_id>')

    @page.url_value_preprocessor
    def hydrate_projects(_: Optional[str], values: Optional[dict[str, Any]]) -> None:
        filters.hydrate_projects(values)

    @page.before_request
    def before_request() -> Optional[ResponseReturnValue]:
        return filters.before_page_request()

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/prompts')
    @page.get('')
    def show() -> ResponseReturnValue:
        prompt_template_versions: list[PromptTemplateVersion] = \
            prompt_template_version_repo.find_all_templates_by_project_id_and_tag(g.project.id)

        templates = [
            PromptListShowFields(
                prompt_template_id=version.prompt_template_id,
                model_name=version.prompt_template_config.model_name if version.prompt_template_config else None,
                last_updated_at=int(version.created_at.timestamp()),
                name=version.name,
                llm_parameters=version.prompt_template_config if version.prompt_template_config else None
            )
            for version in prompt_template_versions
        ]

        return render_template(
            'prompt_list.html',
            project_id=g.project.id,
            new_link=f'/projects/{g.project.id}/new-template',
            project_url=f'/projects/{g.project.id}',
            templates=templates
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/new-template')
    @page.get('/new-chat-template')
    @page.get('/new-text-template')
    def show_new_template() -> ResponseReturnValue:
        llm_model_with_params_list = llm_model_repository.find_all_for_display()
        environments = environments_repo.find_all()

        return render_react(
            'NewPromptTemplateEditor',
            'New Prompt Template',
            hide_main_nav=True,
            project_id=g.project.id,
            default_model_configs=[
                AllowedModelConfigShowFields(llm_model_with_params) for llm_model_with_params in
                llm_model_with_params_list],
            environments=[EnvironmentInfo(env) for env in environments],
        )

    return page
