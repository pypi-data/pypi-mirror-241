import logging
from dataclasses import asdict, dataclass
from operator import and_
from typing import Optional, Any
from uuid import UUID

from dacite import from_dict
from flask import Blueprint, abort, redirect, g, jsonify
from flask import request
from flask.typing import ResponseReturnValue
from sqlalchemy import select, delete

from freeplay_server.accounts.users import Roles
from freeplay_server.auth.auth_filter import allow_role
from freeplay_server.evaluations.eval_page import EvaluationCriteriaInfo
from freeplay_server.extensions import sa
from freeplay_server.models import EvaluationCriteria, EvaluationRubric
from freeplay_server.project_sessions.prompt_model import PromptModel
from freeplay_server.projects.project_page_blueprint_filters import ProjectPageBlueprintFilters
from freeplay_server.prompt_templates.llm_model_parameters import LLMModelParameterValue, LLMModelParameterType, \
    LLMModelParameter
from freeplay_server.prompt_templates.llm_model_repository import LLMModelRepository, \
    LLMModelWithAllowedParametersRecord, LLMAllowedParameter, LLMModelParametersRecord, LLMModelParameterWithValue
from freeplay_server.prompt_templates.prompt_template_version_repository import PromptTemplateUpdateFields, \
    PromptTemplateVersion, PromptTemplateCreationFailure
from freeplay_server.prompt_templates.prompt_template_version_repository import PromptTemplateVersionRepository, \
    LATEST_TAG_NAME
from freeplay_server.settings.settings_repository import EnvironmentsRepository, EnvironmentType
from freeplay_server.utilities.render_react import render_react
from freeplay_server.web_support.json_support import dacite_config

logger = logging.getLogger(__name__)


@dataclass
class PromptTemplateCreateFields:
    name: str
    model_id: Optional[UUID]
    params: Optional[list[LLMModelParameter]]
    content: str
    tags: list[str]


@dataclass
class ModelConfigShowAllowedParameter:
    name: str
    value: Optional[LLMModelParameterValue]
    type: LLMModelParameterType
    is_advanced: bool

    def __init__(self, record: LLMAllowedParameter):
        self.name = record.name
        self.value = record.initial_value
        self.type = record.parameter_type
        self.is_advanced = record.is_advanced


@dataclass
class AllowedModelConfigShowFields:
    model_id: UUID
    name: str
    flavor_name: str
    display_name: str
    deployment_id: Optional[str]
    params: list[ModelConfigShowAllowedParameter]

    def __init__(self, record: LLMModelWithAllowedParametersRecord):
        self.model_id = record.model_id
        self.name = record.model_name
        self.flavor_name = record.flavor_name
        self.display_name = record.display_name or ""
        self.deployment_id = record.deployment_id
        self.params = [ModelConfigShowAllowedParameter(param) for param in record.parameters]


# Prompt template config fields for instances of prompt templates configs.
@dataclass
class PromptTemplateConfigShowParameter:
    name: str
    value: LLMModelParameterValue
    type: LLMModelParameterType

    def __init__(self, record: LLMModelParameterWithValue):
        self.name = record.name
        self.value = record.value
        self.type = record.type


@dataclass
class EnvironmentInfo:
    id: UUID
    name: str
    is_deleted: bool

    def __init__(self, env: EnvironmentType):
        self.id = env.id
        self.name = env.name
        self.is_deleted = env.is_deleted


@dataclass
class PromptTemplateConfigShowFields:
    model_id: UUID
    name: str
    flavor_name: str
    provider_name: str
    params: list[PromptTemplateConfigShowParameter]

    def __init__(self, record: LLMModelParametersRecord):
        self.model_id = record.model_id
        self.name = record.model_name
        self.flavor_name = record.flavor_name
        self.provider_name = record.provider_name
        self.params = [PromptTemplateConfigShowParameter(param) for param in record.parameters]


@dataclass(frozen=True)
class PromptTemplateEditorShowFields:
    project_id: UUID
    prompt_template_id: UUID
    name: str
    content: PromptModel
    prompt_template_version_id: UUID
    prompt_template_config: Optional[PromptTemplateConfigShowFields] = None


@dataclass
class PromptTemplateVersionShowFields:
    id: UUID
    tags: list[str]
    created_at: int
    env_ids: Optional[list[UUID]]
    env_names: Optional[list[str]]
    env_is_deleted: Optional[list[bool]]
    prompt_template_config: Optional[PromptTemplateConfigShowFields] = None


@dataclass
class PromptTemplateEditRenderData:
    template: PromptTemplateEditorShowFields
    default_model_configs: list[AllowedModelConfigShowFields]
    prompt_template_versions: list[PromptTemplateVersionShowFields]

    def __init__(
            self,
            project_id: UUID,
            prompt_template_version: PromptTemplateVersion,
            llm_model_with_params_list: list[LLMModelWithAllowedParametersRecord],
            version_history: list[PromptTemplateVersion]
    ):
        prompt_template_config = PromptTemplateConfigShowFields(
            prompt_template_version.prompt_template_config) if prompt_template_version.prompt_template_config else None
        self.template = PromptTemplateEditorShowFields(
            project_id=project_id,
            prompt_template_id=prompt_template_version.prompt_template_id,
            prompt_template_config=prompt_template_config,
            name=prompt_template_version.name,
            content=PromptModel.from_string(prompt_template_version.content),
            prompt_template_version_id=prompt_template_version.id
        )
        self.default_model_configs = [
            AllowedModelConfigShowFields(llm_model_with_params) for llm_model_with_params in llm_model_with_params_list]
        self.prompt_template_versions = [
            PromptTemplateVersionShowFields(
                id=version.id,
                tags=version.tags or [],
                created_at=int(version.created_at.timestamp()),
                prompt_template_config=PromptTemplateConfigShowFields(
                    version.prompt_template_config
                ) if version.prompt_template_config else None,
                env_names=version.env_names,
                env_ids=version.env_ids,
                env_is_deleted=version.env_is_deleted,
            )
            for version in version_history
        ]


def prompt_templates_page(
        filters: ProjectPageBlueprintFilters,
        prompt_template_version_repo: PromptTemplateVersionRepository,
        llm_model_repository: LLMModelRepository,
        environments_repo: EnvironmentsRepository,
        api_url: str) -> Blueprint:
    page = Blueprint('prompt_templates_page', __name__, url_prefix='/projects/<project_id>/templates')

    @page.url_value_preprocessor
    def hydrate_projects(_: Optional[str], values: Optional[dict[str, Any]]) -> None:
        filters.hydrate_projects(values)

    @page.before_request
    def before_request() -> Optional[ResponseReturnValue]:
        return filters.before_page_request()

    def build_prompt_template_render_data(prompt_template_id: UUID,
                                          version_id: Optional[UUID]) -> PromptTemplateEditRenderData:
        version_history = prompt_template_version_repo.find_all_prompt_template_versions(prompt_template_id)
        version_history.sort(key=lambda v: v.created_at, reverse=True)

        if version_id:
            prompt_template_version = next(ptv for ptv in version_history if ptv.id == version_id)
        else:
            prompt_template_version = version_history[0]
        return PromptTemplateEditRenderData(
            g.project.id,
            prompt_template_version,
            llm_model_repository.find_all_for_display(),
            version_history)

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/<uuid:prompt_template_id>')
    @page.get('/<uuid:prompt_template_id>/versions/<uuid:version_id>')
    def show_prompt_template(prompt_template_id: UUID, version_id: Optional[UUID] = None) -> ResponseReturnValue:
        render_data = build_prompt_template_render_data(prompt_template_id, version_id)
        evaluation_criteria = sa.session.query(EvaluationCriteria).filter_by(
            prompt_template_id=prompt_template_id).all()

        return render_react(
            component='PromptTemplateShowPage',
            title='Prompt Template',
            hide_main_nav=True,
            prompt_template_versions=render_data.prompt_template_versions,
            evaluation_criteria=[EvaluationCriteriaInfo(ec) for ec in evaluation_criteria],
            api_url=api_url,
            **asdict(render_data.template),
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/<uuid:prompt_template_id>/edit')
    @page.get('/<uuid:prompt_template_id>/edit/<uuid:version_id>')
    def edit_prompt_template(prompt_template_id: UUID, version_id: Optional[UUID] = None) -> ResponseReturnValue:
        render_data = build_prompt_template_render_data(prompt_template_id, version_id)
        environments = environments_repo.find_all()

        return render_react(
            component='UpdatePromptTemplateEditor',
            title='Prompt Template Editor',
            hide_main_nav=True,
            template=render_data.template,
            default_model_configs=render_data.default_model_configs,
            prompt_template_versions=render_data.prompt_template_versions,
            environments=[EnvironmentInfo(env) for env in environments],
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/<uuid:prompt_template_id>/evaluation_criteria')
    @page.post('/<uuid:prompt_template_id>/evaluation_criteria/<uuid:evaluation_criteria_id>')
    def save_evaluation_criteria(prompt_template_id: UUID,
                                 evaluation_criteria_id: Optional[UUID] = None) -> ResponseReturnValue:

        evaluation_criteria = EvaluationCriteria(
            prompt_template_id=prompt_template_id,
            name=request.form.get('name', ''),
            question=request.form.get('question', ''),
            type=request.form.get('type', ''),
            llm_eval_enabled=request.form.get('llm_eval_enabled') == 'on',
            llm_question=request.form.get('llm_question', ''),
        )

        evaluation_criteria.rubric = []
        for key, value in request.form.items():
            if key.startswith('rubric-'):
                score = key.split('-')[1]
                evaluation_criteria.rubric.append(EvaluationRubric(score=score, instructions=value))

        if evaluation_criteria_id:
            loaded_criteria = sa.session.get(EvaluationCriteria, evaluation_criteria_id)
            if not loaded_criteria:
                abort(404)
            for rubric in loaded_criteria.rubric:
                sa.session.delete(rubric)
            loaded_criteria.name = evaluation_criteria.name
            loaded_criteria.question = evaluation_criteria.question
            loaded_criteria.llm_eval_enabled = evaluation_criteria.llm_eval_enabled
            loaded_criteria.llm_question = evaluation_criteria.llm_question
            loaded_criteria.rubric = evaluation_criteria.rubric
        else:
            sa.session.add(evaluation_criteria)

        sa.session.commit()
        return redirect(f'/projects/{g.project.id}/templates/{prompt_template_id}')

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/<uuid:prompt_template_id>/evaluation_criteria')
    @page.get('/<uuid:prompt_template_id>/evaluation_criteria/<uuid:evaluation_criteria_id>')
    def evaluation_criteria_page(prompt_template_id: UUID,
                                 evaluation_criteria_id: Optional[UUID] = None) -> ResponseReturnValue:
        version_history = prompt_template_version_repo.find_all_prompt_template_versions(prompt_template_id)
        prompt_name = version_history[0].name

        if evaluation_criteria_id:
            evaluation_criteria = EvaluationCriteriaInfo(sa.session.execute(
                select(EvaluationCriteria).where(EvaluationCriteria.id == evaluation_criteria_id)
            ).scalar_one())
        else:
            evaluation_criteria = None

        return render_react(
            component='EvaluationCriteria',
            title='Evaluation Criteria',
            prompt_template_id=prompt_template_id,
            prompt_name=prompt_name,
            evaluation_criteria=evaluation_criteria,
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.post(
        '/<uuid:prompt_template_id>/evaluation_criteria/delete_evaluation_criteria/<uuid:evaluation_criteria_id>')
    def delete_evaluation_criteria(
            prompt_template_id: UUID,
            evaluation_criteria_id: UUID
    ) -> ResponseReturnValue:
        sa.session.execute(
            delete(EvaluationCriteria)
            .where(
                and_(
                    EvaluationCriteria.id == evaluation_criteria_id,
                    EvaluationCriteria.prompt_template_id == prompt_template_id
                )
            )
        )

        sa.session.commit()

        return redirect(f'/projects/{g.project.id}/templates/{prompt_template_id}')

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/<uuid:prompt_template_id>')
    def save_prompt_template(prompt_template_id: UUID) -> ResponseReturnValue:
        template = from_dict(data_class=PromptTemplateUpdateFields, data=dict(request.get_json()),
                             config=dacite_config())
        if template is None:
            return redirect(f'/projects/{g.project.id}')

        latest_environment = environments_repo.try_find_by_name(LATEST_TAG_NAME)
        if latest_environment and str(latest_environment.name) not in template.tags:
            response = jsonify({"message": 'Missing latest tag'})
            response.status_code = 400
            return response

        version_result = prompt_template_version_repo.update_template(g.project.id, template)
        if isinstance(version_result, PromptTemplateCreationFailure):
            response = jsonify({"message": version_result.value})
            response.status_code = 400
            return response

        return redirect(f'/projects/{g.project.id}/templates/{prompt_template_id}')

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('')
    def save_new_template() -> ResponseReturnValue:
        new_template = from_dict(
            data_class=PromptTemplateCreateFields,
            data=dict(request.get_json()),
            config=dacite_config())

        if not new_template:
            logger.warning(
                f"Received unhandled prompt template: {request.get_json()}")
            response = jsonify({"message": 'Something went wrong'})
            response.status_code = 400
            return response

        latest_environment = environments_repo.try_find_by_name(LATEST_TAG_NAME)
        if latest_environment and str(latest_environment.name) not in new_template.tags:
            response = jsonify({"message": 'Missing latest tag'})
            response.status_code = 400
            return response

        version_result = prompt_template_version_repo.create_template(
            project_id=g.project.id,
            name=new_template.name,
            content=new_template.content,
            tags=new_template.tags,
            model_id=new_template.model_id,
            model_params=new_template.params
        )

        if isinstance(version_result, PromptTemplateCreationFailure):
            response = jsonify({"message": version_result.value})
            response.status_code = 400
            return response

        return redirect(f'/projects/{g.project.id}')

    return page
