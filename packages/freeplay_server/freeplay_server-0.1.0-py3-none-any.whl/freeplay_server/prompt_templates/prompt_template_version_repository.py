from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional, Union, List
from uuid import UUID

from sqlalchemy.engine import Connection

from freeplay_server.database_support.database_gateway import DatabaseGateway
from freeplay_server.prompt_templates.llm_model_parameters import LLMModelParameter
from freeplay_server.prompt_templates.llm_model_repository import LLMModelRepository, LLMModelParametersRecord
from freeplay_server.settings.settings_repository import EnvironmentType, EnvironmentsRepository


@dataclass(frozen=True)
class _PromptTemplateVersionRow:
    prompt_template_id: UUID
    model_id: Optional[UUID]
    name: str
    content: str
    created_at: datetime
    id: UUID
    deployment_id: Optional[str]
    api_version: Optional[str]
    resource_name: Optional[str]
    tags: Optional[List[str]] = None
    env_ids: Optional[List[UUID]] = None
    env_names: Optional[List[str]] = None
    env_is_deleted: Optional[list[bool]] = None
    model_config_id: Optional[UUID] = None


@dataclass(frozen=True)
class PromptTemplateVersion:
    prompt_template_id: UUID
    name: str
    content: str
    created_at: datetime
    id: UUID
    deployment_id: Optional[str]
    api_version: Optional[str]
    resource_name: Optional[str]
    prompt_template_config: Optional[LLMModelParametersRecord]
    tags: List[str]
    env_names: List[str]
    env_ids: List[UUID]
    env_is_deleted: Optional[list[bool]]


@dataclass(frozen=True)
class PromptTemplateVersionRecordIds:
    prompt_template_id: UUID
    prompt_template_version_id: UUID


@dataclass(frozen=True)
class PromptTemplateVersionTaggedRecord:
    id: UUID
    prompt_template_version_id: UUID
    environment: UUID


@dataclass(frozen=True)
class PromptTemplateUpdateFields:
    prompt_template_id: UUID
    name: str
    content: str
    tags: list[str]
    model_id: Optional[UUID] = None
    params: Optional[list[LLMModelParameter]] = None


class PromptTemplateCreationFailure(Enum):
    NameAlreadyTaken = 'This name is already taken'


PromptTemplateResult = Union[
    PromptTemplateVersionRecordIds,
    PromptTemplateCreationFailure,
]

LATEST_TAG_NAME = 'latest'


class PromptTemplateVersionRepository:

    def __init__(self,
                 db: DatabaseGateway,
                 llm_model_repository: LLMModelRepository,
                 environments_repository: EnvironmentsRepository):
        self.db = db
        self.llm_model_repository = llm_model_repository
        self.environments_repository = environments_repository

    def create_template(
            self,
            project_id: UUID,
            name: str,
            content: str,
            tags: list[str],
            model_id: Optional[UUID] = None,
            model_params: Optional[list[LLMModelParameter]] = None
    ) -> PromptTemplateResult:
        with self.db.transaction() as connection:
            name_exists = self.db.exists(
                'select count(id) from prompt_templates where project_id = :project_id and name = :name',
                connection,
                project_id=project_id,
                name=name,
            )

            if name_exists:
                return PromptTemplateCreationFailure.NameAlreadyTaken

            prompt_template_id = self.__create_template_record(connection, project_id, name)

            model_config_id = (
                None
                if model_id is None
                else self.llm_model_repository.create_model_config(
                    connection,
                    model_id=model_id,
                    model_params=model_params or []
                )
            )

            prompt_template_version_id = \
                self.__create_template_version(connection, prompt_template_id, content, model_config_id)

            self.update_template_tags(prompt_template_version_id, prompt_template_id, tags, connection)

        return PromptTemplateVersionRecordIds(
            prompt_template_id=prompt_template_id,
            prompt_template_version_id=prompt_template_version_id,
        )

    def update_template(self, project_id: UUID, template: PromptTemplateUpdateFields) -> PromptTemplateResult:
        with self.db.transaction() as connection:
            name_exists = self.db.exists(
                """
                select count(id) from prompt_templates 
                where project_id = :project_id and name = :name and id <> :prompt_template_id
                """,
                connection,
                project_id=project_id,
                name=template.name,
                prompt_template_id=template.prompt_template_id
            )

            if name_exists:
                return PromptTemplateCreationFailure.NameAlreadyTaken

            model_config_id = (
                self.llm_model_repository.create_model_config(
                    connection, model_id=template.model_id, model_params=template.params or []
                )
                if template.model_id is not None
                else None
            )

            self.__update_template_name(
                connection,
                template_id=template.prompt_template_id,
                name=template.name
            )
            prompt_template_version_id = self.__create_template_version(
                connection,
                prompt_template_id=template.prompt_template_id,
                model_config_id=model_config_id,
                content=template.content,
            )

            self.update_template_tags(prompt_template_version_id, template.prompt_template_id, template.tags,
                                      connection)

        return PromptTemplateVersionRecordIds(
            prompt_template_id=template.prompt_template_id,
            prompt_template_version_id=prompt_template_version_id,
        )

    def update_template_tags(
            self,
            prompt_template_version_id: UUID,
            prompt_template_id: UUID,
            tags: list[str],
            connection: Optional[Connection] = None) -> UUID:

        tags_id = []
        for tag in tags:
            tags_id.append(self.environments_repository.check_and_create_environment(tag, connection=connection))

        if connection is None:
            with self.db.transaction() as connection:
                for tag in tags_id:
                    self.__tag_prompt_template_version(connection, prompt_template_version_id, prompt_template_id, tag)
        else:
            for tag in tags_id:
                self.__tag_prompt_template_version(connection, prompt_template_version_id, prompt_template_id, tag)

        return prompt_template_version_id

    def find_template_version_by_ids(
            self,
            prompt_template_version_ids: list[UUID],
            connection: Optional[Connection] = None
    ) -> dict[UUID, PromptTemplateVersion]:
        if not prompt_template_version_ids:
            return {}

        rows = self.db.find_all(_PromptTemplateVersionRow, """
                    select 
                        prompt_template_versions.prompt_template_id as prompt_template_id, 
                        prompt_template_versions.id as id,
                        prompt_template_model_configs.model_id as model_id,
                        prompt_templates.name as name,
                        prompt_template_versions.content as content,
                        prompt_template_versions.created_at as created_at,
                        prompt_template_versions.model_config_id as model_config_id
                    from prompt_template_versions
                        inner join prompt_templates on prompt_template_versions.prompt_template_id = prompt_templates.id
                        left join prompt_template_model_configs on prompt_template_versions.model_config_id = prompt_template_model_configs.id
                    where prompt_template_versions.id in :prompt_template_version_ids
                """,
                                prompt_template_version_ids=tuple(prompt_template_version_ids),
                                connection=connection)
        hydrated_prompts = self.__hydrate_prompt_template_version_model_configs(rows)
        return {prompt.id: prompt for prompt in hydrated_prompts}

    def find_all_templates_by_project_id_and_tag(
            self,
            project_id: UUID,
            tag: str = LATEST_TAG_NAME,
            connection: Optional[Connection] = None
    ) -> list[PromptTemplateVersion]:
        rows = self.db.find_all(_PromptTemplateVersionRow, """
            select 
                prompt_template_versions.prompt_template_id as prompt_template_id, 
                prompt_template_versions.id as id,
                prompt_template_model_configs.model_id as model_id,
                prompt_templates.name as name,
                prompt_template_versions.content as content,
                prompt_template_versions.created_at as created_at,
                prompt_template_versions.model_config_id as model_config_id,
                emc.name as resource_name,
                emc.deployment_id as deployment_id,
                emc.api_version as api_version
            from prompt_template_versions
                inner join prompt_templates on prompt_template_versions.prompt_template_id = prompt_templates.id
                inner join projects on prompt_templates.project_id = projects.id
                inner join prompt_template_tagged_versions on prompt_template_versions.id = prompt_template_tagged_versions.prompt_template_version_id
                left join prompt_template_model_configs on prompt_template_versions.model_config_id = prompt_template_model_configs.id
                inner join environments on prompt_template_tagged_versions.environment = environments.id
                left join llm_models lm on lm.id = prompt_template_model_configs.model_id
                left join endpoint_model_configs emc on lm.id = emc.model_id
            where projects.id = :project_id and environments.name = :environment
        """, connection=connection, project_id=project_id, environment=tag, )
        return self.__hydrate_prompt_template_version_model_configs(rows)

    def find_all_prompt_template_versions(self, prompt_template_id: UUID) -> list[PromptTemplateVersion]:
        rows = self.db.find_all(_PromptTemplateVersionRow, """
            select
                prompt_template_versions.prompt_template_id as prompt_template_id, 
                prompt_template_versions.id as id,
                prompt_template_model_configs.model_id as model_id,
                prompt_templates.name as name,
                prompt_template_versions.content as content,
                prompt_template_versions.created_at as created_at,
                prompt_template_versions.model_config_id as model_config_id,
                array_remove(array_agg(environments.id), NULL) as env_ids,
                array_remove(array_agg(environments.name), NULL) as env_names,
                array_remove(array_agg(environments.is_deleted), NULL) as env_is_deleted
            from prompt_template_versions
                inner join prompt_templates on prompt_template_versions.prompt_template_id = prompt_templates.id
                left join prompt_template_tagged_versions on prompt_template_versions.id = prompt_template_tagged_versions.prompt_template_version_id
                left join environments on prompt_template_tagged_versions.environment = environments.id
                left join prompt_template_model_configs on prompt_template_versions.model_config_id = prompt_template_model_configs.id
            where prompt_templates.id = :prompt_template_id
            group by prompt_template_id, prompt_template_versions.id, model_id, prompt_templates.name, content, created_at, model_config_id
        """, prompt_template_id=prompt_template_id)

        return self.__hydrate_prompt_template_version_model_configs(rows)

    def __hydrate_prompt_template_version_model_configs(
            self,
            rows: list[_PromptTemplateVersionRow]
    ) -> list[PromptTemplateVersion]:
        all_model_config_ids = [ptv.model_config_id for ptv in rows if ptv.model_config_id]
        model_configs = self.llm_model_repository.find_all_by_model_config_ids(all_model_config_ids)

        hydrated_versions = []
        for prompt_template_version in rows:
            try:
                model_config_for_version = next(
                    model_config for model_config in model_configs if
                    model_config.model_config_id == prompt_template_version.model_config_id)
            except StopIteration:
                # No match found. This is a valid state - set model_config_for_version to None.
                model_config_for_version = None
            hydrated_versions.append(PromptTemplateVersion(
                prompt_template_version.prompt_template_id,
                prompt_template_version.name,
                prompt_template_version.content,
                prompt_template_version.created_at,
                prompt_template_version.id,
                deployment_id=prompt_template_version.deployment_id,
                api_version=prompt_template_version.api_version,
                resource_name=prompt_template_version.resource_name,
                prompt_template_config=model_config_for_version,
                tags=prompt_template_version.tags if prompt_template_version.tags else [],
                env_names=prompt_template_version.env_names if prompt_template_version.env_names else [],
                env_ids=prompt_template_version.env_ids if prompt_template_version.env_ids else [],
                env_is_deleted=prompt_template_version.env_is_deleted if prompt_template_version.env_is_deleted else [],
            ))

        return hydrated_versions

    def delete_template(self, template_id: UUID) -> None:
        with self.db.transaction() as connection:
            model_config_ids = self.db.find_all_ids(
                sql="select model_config_id as id from prompt_template_versions where prompt_template_id = :id",
                connection=connection, id=template_id
            )
            self.db.execute(
                "delete from prompt_template_versions where prompt_template_id = :id",
                connection, id=template_id
            )
            self.db.execute(
                "delete from prompt_template_model_configs where id in :model_config_ids",
                connection, model_config_ids=tuple(model_config_ids)
            )
            self.db.execute(
                "delete from prompt_templates where id=:id",
                connection, id=template_id
            )

    def prompt_names(self, project_id: UUID) -> list[str]:
        @dataclass
        class Row:
            name: str

        return [r.name for r in self.db.find_all(
            type=Row,
            sql="select name from prompt_templates where project_id = :project_id",
            project_id=project_id,
        )]

    def __update_template_name(self, connection: Connection, template_id: UUID, name: str) -> None:
        self.db.execute(
            "update prompt_templates set name = :name where id = :id",
            connection,
            id=template_id,
            name=name,
        )

    def __create_template_version(self,
                                  connection: Connection,
                                  prompt_template_id: UUID,
                                  content: str,
                                  model_config_id: Optional[UUID] = None) -> UUID:
        return self.db.create_returning_id(
            """
            insert into prompt_template_versions (prompt_template_id, model_config_id, content)
            values (:prompt_template_id, :model_config_id, :content)
            returning id
            """,
            connection,
            prompt_template_id=prompt_template_id,
            model_config_id=model_config_id,
            content=content,
        )

    def __create_template_record(self, connection: Connection, project_id: UUID, name: str) -> UUID:
        return self.db.create_returning_id(
            """
            insert into prompt_templates (project_id, name) 
            values (:project_id, :name) 
            returning id
            """,
            connection,
            project_id=project_id,
            name=name
        )

    def __tag_prompt_template_version(self,
                                      connection: Connection,
                                      prompt_template_version_id: UUID,
                                      prompt_template_id: UUID,
                                      tag: str) -> None:
        existing_tagged_version = self.db.try_find(PromptTemplateVersionTaggedRecord, """
                       select prompt_template_tagged_versions.*
                       from prompt_template_tagged_versions
                            join prompt_template_versions on prompt_template_tagged_versions.prompt_template_version_id = prompt_template_versions.id
                            join environments on prompt_template_tagged_versions.environment = environments.id
                       where environments.id = :environment and prompt_template_versions.prompt_template_id = :prompt_template_id
                   """, connection, environment=tag, prompt_template_id=prompt_template_id)

        if existing_tagged_version is None:
            environment = self.db.try_find(
                type=EnvironmentType,
                sql="""
                    SELECT id, name, created_date, is_deleted
                    FROM environments
                    WHERE environments.id = :environment
                """,
                connection=connection,
                environment=tag)
            if environment is not None:
                self.db.execute(
                    """
                    insert into prompt_template_tagged_versions (prompt_template_version_id, environment)
                    values (:prompt_template_version_id, :environment)
                    """,
                    connection,
                    prompt_template_version_id=prompt_template_version_id,
                    environment=environment.id,
                )
        else:
            self.db.execute(
                """
                update prompt_template_tagged_versions set prompt_template_version_id = :prompt_template_version_id 
                where id = :id 
                """,
                connection,
                id=existing_tagged_version.id,
                prompt_template_version_id=prompt_template_version_id,
            )
