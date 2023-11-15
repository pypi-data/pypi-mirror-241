from dataclasses import dataclass
from typing import List, Optional
from uuid import UUID

from sqlalchemy.engine import Connection

from freeplay_server.database_support.database_gateway import DatabaseGateway
from freeplay_server.prompt_templates.llm_model_parameters import LLMModelParameterValue, LLMModelParameterType, \
    parse_model_parameter_from_string, LLMModelParameter, UnexpectedParameterError


@dataclass
class _LLMModelParameterWithValueRow:
    model_config_id: UUID
    model_id: UUID
    model_name: str
    flavor_name: str
    provider_name: str
    parameter_names: list[str]
    parameter_types: list[str]
    parameter_values: list[str]


@dataclass
class LLMModelParameterWithValue:
    name: str
    value: LLMModelParameterValue
    type: LLMModelParameterType


@dataclass
class LLMModelParametersRecord:
    model_id: UUID
    model_name: str
    flavor_name: str
    provider_name: str
    model_config_id: UUID
    parameters: list[LLMModelParameterWithValue]


@dataclass
class _LLMAllowedParameterRow:
    model_id: UUID
    model_name: str
    flavor_name: str
    deployment_id: Optional[str]
    parameter_ids: list[UUID]
    parameter_names: list[str]
    parameter_types: list[str]
    initial_values: list[Optional[str]]
    is_advanced_list: list[bool]
    allow_record_list: list[bool]
    display_name: Optional[str] = None


@dataclass
class LLMAllowedParameter:
    id: UUID
    name: str
    initial_value: Optional[LLMModelParameterValue]
    parameter_type: LLMModelParameterType
    is_advanced: bool
    allow_record: bool


@dataclass
class LLMModelWithAllowedParametersRecord:
    model_id: UUID
    model_name: str
    flavor_name: str
    parameters: list[LLMAllowedParameter]
    deployment_id: Optional[str] = None
    display_name: Optional[str] = None


@dataclass
class LLMModelRecord:
    id: UUID
    name: str


class LLMModelRepository:
    def __init__(self, db: DatabaseGateway) -> None:
        self.db = db

    def find_all_for_display(self) -> List[LLMModelWithAllowedParametersRecord]:
        rows = self.db.find_all(
            type=_LLMAllowedParameterRow,
            sql="""
                SELECT
                    lm.id as model_id,
                    lm.name as model_name,
                    llm_flavors.name as flavor_name,
                    llm_flavors.display_name as display_name,
                    emc.deployment_id as deployment_id,
                    array_remove(array_agg(lmap.id), null) as parameter_ids,
                    array_remove(array_agg(lmap.name), null) as parameter_names,
                    array_remove(array_agg(lmap.type), null) as parameter_types,
                    array_agg(lmap.initial_value) as initial_values,
                    array_remove(array_agg(lmap.is_advanced), null) as is_advanced_list,
                    array_remove(array_agg(lmap.allow_record), null) as allow_record_list
                FROM
                    endpoint_model_configs emc
                JOIN llm_models lm ON emc.model_id = lm.id
                LEFT JOIN llm_model_allowed_parameters lmap ON lm.id = lmap.model_id
                JOIN llm_flavors ON lm.flavor_id = llm_flavors.id
                WHERE
                    lm.is_visible = true
                    AND lmap.ui_configurable
                GROUP BY
                    lm.id,
                    lm.name,
                    llm_flavors.name,
                    llm_flavors.display_name,
                    emc.deployment_id
        """)
        azure_rows = self.__map_llm_model_allowed_params_to_records(rows)

        rows = self.db.find_all(
            type=_LLMAllowedParameterRow,
            sql="""
                SELECT
                    llm_models.id as model_id,
                    llm_models.name as model_name,
                    llm_flavors.name as flavor_name,
                    llm_flavors.display_name as display_name,
                    null as deployment_id,
                    array_remove(array_agg(llm_model_allowed_parameters.id), null) as parameter_ids,
                    array_remove(array_agg(llm_model_allowed_parameters.name), null) as parameter_names,
                    array_remove(array_agg(llm_model_allowed_parameters.type), null) as parameter_types,
                    array_agg(llm_model_allowed_parameters.initial_value) as initial_values,
                    array_remove(array_agg(llm_model_allowed_parameters.is_advanced), null) as is_advanced_list,
                    array_remove(array_agg(llm_model_allowed_parameters.allow_record), null) as allow_record_list
                FROM
                    llm_models
                LEFT JOIN llm_model_allowed_parameters ON llm_models.id = llm_model_allowed_parameters.model_id
                JOIN llm_flavors ON llm_models.flavor_id = llm_flavors.id
                WHERE
                    llm_models.is_visible = true
                    AND llm_model_allowed_parameters.ui_configurable
                    AND llm_flavors.is_active
                GROUP BY
                    llm_models.id,
                    llm_models.name,
                    llm_flavors.name,
                    llm_flavors.display_name
                ORDER BY
                    flavor_name ASC;
        """)
        default_models_rows = self.__map_llm_model_allowed_params_to_records(rows)
        default_models_rows.extend(azure_rows)
        return default_models_rows

    def try_find_model_with_params(self, model_id: UUID) -> Optional[LLMModelWithAllowedParametersRecord]:
        llm_allowed_parameter_row = self.db.try_find(
            type=_LLMAllowedParameterRow,
            sql="""
                select
                    llm_models.id as model_id,
                    llm_models.name as model_name,
                    llm_flavors.name as flavor_name,
                    -- Use array_remove to strip [null] values from array_agg response.
                    array_remove(array_agg(llm_model_allowed_parameters.id), NULL)  as parameter_ids,
                    array_remove(array_agg(llm_model_allowed_parameters.name), NULL)  as parameter_names,
                    array_remove(array_agg(llm_model_allowed_parameters.type), NULL) as parameter_types,
                    -- initial_values are nullable in the DB so we want to allow NULL values here
                    array_agg(llm_model_allowed_parameters.initial_value) as initial_values,
                    array_remove(array_agg(llm_model_allowed_parameters.is_advanced), NULL) as is_advanced_list,
                    array_remove(array_agg(llm_model_allowed_parameters.allow_record), NULL) as allow_record_list
                from llm_models
                    join llm_model_allowed_parameters on llm_models.id = llm_model_allowed_parameters.model_id
                    join llm_flavors on llm_models.flavor_id = llm_flavors.id
                where llm_models.is_visible = true
                    and llm_models.id =:model_id
                group by llm_models.id, llm_models.name, llm_flavors.name
                order by llm_models.name DESC
            """,
            model_id=model_id
        )

        if not llm_allowed_parameter_row:
            return None

        return self.__map_llm_model_allowed_params_to_record(llm_allowed_parameter_row)

    def find_models_by_ids(self, model_ids: set[UUID]) -> dict[UUID, str]:
        if len(model_ids) == 0:
            return dict()

        rows = self.db.find_all(
            type=LLMModelRecord,
            sql="""
                       select
                           llm_models.id as id,
                           llm_models.name as name
                       from llm_models
                       where llm_models.id in :model_ids
                   """, model_ids=tuple(model_ids))

        return dict((model.id, model.name) for model in rows)

    def find_all_by_model_config_ids(self, model_config_ids: list[UUID]) -> list[LLMModelParametersRecord]:
        if len(model_config_ids) == 0:
            return list()

        rows = self.db.find_all(
            type=_LLMModelParameterWithValueRow,
            sql="""
                select
                    llm_models.id as model_id,
                    llm_models.name as model_name,
                    prompt_template_model_configs.id as model_config_id,
                    llm_flavors.name  as flavor_name,
                    llm_flavors.provider_name as provider_name,
                    -- Use array_remove to strip [null] values from array_agg response.
                    array_remove(ARRAY_AGG(llm_model_allowed_parameters.name), NULL) as parameter_names,
                    array_remove(ARRAY_AGG(llm_model_allowed_parameters.type), NULL) as parameter_types,
                    array_remove(ARRAY_AGG(llm_model_parameter_values.value), NULL) as parameter_values
                from prompt_template_model_configs
                    join llm_models on llm_models.id=prompt_template_model_configs.model_id
                    join llm_flavors on llm_models.flavor_id = llm_flavors.id
                    left join llm_model_parameter_values on prompt_template_model_configs.id = llm_model_parameter_values.prompt_template_model_config_id
                    left join llm_model_allowed_parameters on llm_model_parameter_values.parameter_id=llm_model_allowed_parameters.id
                where prompt_template_model_configs.id in :model_config_ids
                group by llm_models.id, llm_models.name, prompt_template_model_configs.id, llm_flavors.name, llm_flavors.provider_name
                order by llm_models.name DESC
            """, model_config_ids=tuple(model_config_ids)
        )
        return self.__map_llm_model_params_to_records(rows)

    def try_find_model_by_provider_and_name(self, model_name: str, provider_name: str) -> Optional[LLMModelRecord]:
        return self.db.try_find(type=LLMModelRecord, sql="""
            SELECT lm.id, lm.name
            FROM llm_models lm
                JOIN llm_flavors lf on lm.flavor_id = lf.id
            WHERE lm.name=:model_name
                AND lf.provider_name=:provider_name;
        """, model_name=model_name, provider_name=provider_name)

    def find_recordable_parameters_for_model_id(self, model_id: UUID) -> dict[str, LLMAllowedParameter]:
        llm_parameter_id_by_name: dict[str, LLMAllowedParameter] = {}
        model_with_params = self.try_find_model_with_params(model_id)
        if model_with_params:
            for param in model_with_params.parameters:
                if param.allow_record:
                    llm_parameter_id_by_name[param.name] = param
        return llm_parameter_id_by_name

    def model_names(self) -> list[str]:
        @dataclass
        class Row:
            name: str

        return [r.name for r in self.db.find_all(
            type=Row,
            sql="select name from llm_models",
        )]

    def create_model_config(
            self,
            connection: Connection,
            model_id: UUID,
            model_params: list[LLMModelParameter]
    ) -> UUID:
        prompt_template_model_config_id = self.db.create_returning_id(
            """
                insert into prompt_template_model_configs (model_id) VALUES (:model_id)
                returning id 
            """,
            connection=connection,
            model_id=model_id
        )

        try:
            for param in model_params:
                self.db.create_returning_id(
                    """
                        insert into llm_model_parameter_values (prompt_template_model_config_id, parameter_id, value)
                        SELECT :prompt_template_model_config_id, id, :parameter_value from llm_model_allowed_parameters
                        WHERE model_id=:model_id AND name=:parameter_name AND type=:parameter_type
                        returning id
                    """,
                    connection=connection,
                    prompt_template_model_config_id=prompt_template_model_config_id,
                    model_id=model_id,
                    parameter_name=param.name,
                    parameter_value=str(param.value),
                    parameter_type=param.type.value
                )
        except Exception as e:
            raise UnexpectedParameterError("Unexpected LLM parameter provided to create model configuration")

        return prompt_template_model_config_id

    @staticmethod
    def __map_llm_model_allowed_params_to_records(
            rows: list[_LLMAllowedParameterRow]
    ) -> list[LLMModelWithAllowedParametersRecord]:
        output = []
        for row in rows:
            output.append(LLMModelRepository.__map_llm_model_allowed_params_to_record(row))

        return output

    @staticmethod
    def __map_llm_model_allowed_params_to_record(
            row: _LLMAllowedParameterRow
    ) -> LLMModelWithAllowedParametersRecord:
        params = []
        for i in range(0, len(row.parameter_names)):
            parameter_type = row.parameter_types[i]
            maybe_initial_value = row.initial_values[i]
            initial_value = parse_model_parameter_from_string(LLMModelParameterType(parameter_type),
                                                              maybe_initial_value) if maybe_initial_value is not None else None
            params.append(
                LLMAllowedParameter(
                    row.parameter_ids[i],
                    row.parameter_names[i],
                    initial_value,
                    LLMModelParameterType(parameter_type),
                    row.is_advanced_list[i],
                    row.allow_record_list[i]
                )
            )

        params.sort(key=lambda p: p.name)
        return LLMModelWithAllowedParametersRecord(
            model_id=row.model_id,
            flavor_name=row.flavor_name,
            model_name=row.model_name,
            display_name=row.display_name,
            deployment_id=row.deployment_id,
            parameters=params
        )

    @staticmethod
    def __map_llm_model_params_to_records(
            rows: list[_LLMModelParameterWithValueRow]
    ) -> list[LLMModelParametersRecord]:
        output = []
        for row in rows:
            params = []
            for i in range(0, len(row.parameter_names)):
                parameter_type = LLMModelParameterType(row.parameter_types[i])
                params.append(LLMModelParameterWithValue(
                    row.parameter_names[i],
                    parse_model_parameter_from_string(
                        parameter_type, row.parameter_values[i]),
                    parameter_type
                ))

            params.sort(key=lambda p: p.name)
            output.append(LLMModelParametersRecord(
                model_id=row.model_id,
                model_name=row.model_name,
                flavor_name=row.flavor_name,
                provider_name=row.provider_name,
                model_config_id=row.model_config_id,
                parameters=params
            ))

        return output
