import logging
import time
from _decimal import Decimal
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any, TypeVar, Union
from uuid import UUID

from sqlalchemy import ColumnElement, ScalarSelect, and_, exists, or_, select, Select, not_
from sqlalchemy import func, distinct
from sqlalchemy.engine import Connection
from sqlalchemy.orm import aliased, InstrumentedAttribute

from freeplay_server.auth.api_keys_repository import ApiKeysRepository
from freeplay_server.database_support.database_gateway import DatabaseGateway
from freeplay_server.extensions import sa
from freeplay_server.models import EvaluationCriteria, EvaluationResult, ProjectSession, ProjectSessionEntry, \
    ProjectSessionEntryInputs, \
    LLMModel, LLMFlavor, PromptTemplate, Environment
from freeplay_server.project_sessions.project_sessions import ProjectSessionCalculator
from freeplay_server.project_sessions.prompt_model import PromptModel
from freeplay_server.prompt_templates.llm_model_parameters import LLMModelParameterType, UnexpectedParameterError
from freeplay_server.prompt_templates.llm_model_repository import LLMModelRepository, LLMAllowedParameter
from freeplay_server.web_support import json_support

logger = logging.getLogger(__name__)


@dataclass
class FunctionCall:
    name: str
    arguments: str


@dataclass
class _ProjectSessionsRow:
    id: UUID
    project_id: UUID
    logged_at: datetime
    input_names: list[str]
    input_values: list[str]
    response: str
    prompt_template_id: UUID
    prompt_template_version_id: UUID


@dataclass
class ProjectSessionsRecord:
    id: UUID
    project_id: UUID
    logged_at: datetime
    inputs: dict[str, str]
    response: str
    prompt_template_id: UUID
    prompt_template_version_id: UUID


@dataclass
class ProjectSessionUniqueProvidersRecord:
    llm_model_name: str
    llm_provider_name: str


@dataclass
class _ProjectSessionListRow:
    id: UUID
    logged_at: datetime
    response: str
    input_names: list[str]
    input_values: list[str]
    models: list[str]
    providers: list[str]
    prompt_names: list[str]


@dataclass
class _ProjectSessionDetailsRow:
    session_id: UUID
    id: UUID
    logged_at: datetime
    input_names: list[str]
    input_values: list[str]
    llm_model: Optional[str]
    llm_provider: Optional[str]
    param_names: list[str]
    param_values: list[str]
    response: str
    template_content: str
    api_key_name: Optional[str]
    prompt_template_id: UUID
    prompt_template_version_id: UUID
    template_name: str
    format_type: Optional[str]
    is_complete: Optional[bool]
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    interpolated_prompt_content: Optional[str]
    prompt_token_count: Optional[int]
    response_token_count: Optional[int]
    prompt_token_cost: Optional[Decimal]
    response_token_cost: Optional[Decimal]
    function_call_response: Optional[FunctionCall]
    environment_name: Optional[str]
    is_env_deleted: Optional[bool] = False


@dataclass
class ProjectSessionEntryDetailsRecord:
    id: UUID
    logged_at: datetime
    template_name: str
    prompt_template_id: UUID
    prompt_template_version_id: UUID
    template_content: PromptModel
    inputs: dict[str, str]
    api_key_name: Optional[str]
    llm_model: Optional[str]
    llm_provider: Optional[str]
    llm_parameters: dict[str, str]
    response: str
    format_type: Optional[str]
    is_complete: Optional[bool]
    prompt_token_count: Optional[int]
    return_token_count: Optional[int]
    prompt_token_cost: Optional[Decimal]
    return_token_cost: Optional[Decimal]
    interpolated_prompt_content: Optional[PromptModel]
    session_latency: Optional[Decimal]
    function_call_response: Optional[FunctionCall]
    environment_name: Optional[str]
    is_env_deleted: Optional[bool] = False


@dataclass
class ProjectSessionDetailsRecord:
    id: UUID
    entries: list[ProjectSessionEntryDetailsRecord]
    aggregate_prompt_token_count: Optional[int]
    aggregate_return_token_count: Optional[int]
    aggregate_prompt_token_cost: Optional[Decimal]
    aggregate_return_token_cost: Optional[Decimal]
    aggregate_session_latency: Optional[Decimal]


@dataclass
class FilterConfig:
    filterType: str
    type: Optional[str]
    filter: Union[str, int, float, None]
    dateFrom: Optional[str]
    dateTo: Optional[str]
    values: Optional[list[str]]
    filterTo: Optional[str]


@dataclass
class SessionsDataRequest:
    before_timestamp: float
    filters: dict[str, FilterConfig]
    start_row: int
    end_row: int

    def before_datetime(self) -> datetime:
        return datetime.fromtimestamp(self.before_timestamp)


class FilterError(ValueError):
    def __init__(self, message: str):
        super().__init__(message)


def build_map_from_lists(names: list[str], values: list[str]) -> dict[str, str]:
    inputs = {}
    for i in range(0, len(names)):
        inputs[names[i]] = values[i]

    return inputs


def map_list_row_to_list_record(row: _ProjectSessionsRow) -> ProjectSessionsRecord:
    return ProjectSessionsRecord(
        id=row.id,
        project_id=row.project_id,
        logged_at=row.logged_at,
        inputs=build_map_from_lists(row.input_names, row.input_values),
        response=row.response,
        prompt_template_id=row.prompt_template_id,
        prompt_template_version_id=row.prompt_template_version_id
    )


def try_map_details_rows_to_record(rows: list[_ProjectSessionDetailsRow]) -> Optional[ProjectSessionDetailsRecord]:
    if len(rows) == 0:
        return None

    entries = [
        ProjectSessionEntryDetailsRecord(
            id=row.id,
            logged_at=row.logged_at,
            inputs=build_map_from_lists(row.input_names, row.input_values),
            llm_model=row.llm_model,
            llm_provider=row.llm_provider,
            llm_parameters=build_map_from_lists(row.param_names, row.param_values),
            response=row.response,
            template_name=row.template_name,
            template_content=PromptModel.from_string(row.template_content),
            prompt_template_id=row.prompt_template_id,
            prompt_template_version_id=row.prompt_template_version_id,
            format_type=row.format_type,
            is_complete=row.is_complete,
            interpolated_prompt_content=PromptModel.from_string(row.interpolated_prompt_content),
            prompt_token_count=row.prompt_token_count,
            return_token_count=row.response_token_count,
            prompt_token_cost=row.prompt_token_cost,
            return_token_cost=row.response_token_cost,
            session_latency=ProjectSessionCalculator.calculate_latency(row.start_time, row.end_time),
            function_call_response=row.function_call_response,
            api_key_name=row.api_key_name,
            environment_name=row.environment_name,
            is_env_deleted=row.is_env_deleted,
        )
        for row in rows
    ]

    aggregate_prompt_token_count = sum(
        entry.prompt_token_count for entry in entries if entry.prompt_token_count) or None
    aggregate_return_token_count = sum(
        entry.return_token_count for entry in entries if entry.return_token_count) or None
    aggregate_prompt_token_cost = sum(entry.prompt_token_cost for entry in entries if entry.prompt_token_cost) or None
    aggregate_return_token_cost = sum(entry.return_token_cost for entry in entries if entry.return_token_cost) or None
    aggregate_session_latency = sum(
        [entry.session_latency or Decimal(0) for entry in entries if entry.session_latency], Decimal(0))

    return ProjectSessionDetailsRecord(
        id=rows[0].session_id,
        entries=entries,
        aggregate_prompt_token_count=aggregate_prompt_token_count,
        aggregate_return_token_count=aggregate_return_token_count,
        aggregate_prompt_token_cost=aggregate_prompt_token_cost,
        aggregate_return_token_cost=aggregate_return_token_cost,
        aggregate_session_latency=aggregate_session_latency
    )


@dataclass(frozen=True)
class ProjectSessionSavedIds:
    project_session_id: UUID
    project_session_entry_id: UUID


class ProjectSessionsRepository:

    def __init__(self, db: DatabaseGateway, llm_models_repo: LLMModelRepository,
                 api_key_repo: ApiKeysRepository) -> None:
        self.db = db
        self.llm_models_repo = llm_models_repo
        self.api_key_repo = api_key_repo

    def try_find(self, session_id: UUID) -> Optional[ProjectSessionDetailsRecord]:
        rows = self.db.find_all(
            type=_ProjectSessionDetailsRow,
            sql="""
                select
                    ps.id as session_id,
                    pse.id, pse.logged_at, pse.response, pse.format_type, pse.is_complete,
                    pse.prompt as interpolated_prompt_content, pse.prompt_token_count, pse.response_token_count, 
                    pse.prompt_token_cost, pse.response_token_cost, pse.function_call_response,
                    pse.api_key_name as api_key_name,
                    pse.environment_id as environment_id,
                    env.name as environment_name,
                    env.is_deleted as is_env_deleted,
                    lm.name as llm_model,
                    lf.provider_name as llm_provider,
                    -- Use array_remove to strip [null] values from array_agg response.
                    array_remove(array_agg(psei.name), NULL) as input_names,
                    array_remove(array_agg(psei.value), NULL) as input_values,
                    array_remove(array_agg(lmap.name), NULL)  as param_names,
                    array_remove(array_agg(psellmp.value), NULL) as param_values,
                    ptv.content as template_content,
                    ptv.id as prompt_template_version_id,
                    pt.name as template_name,
                    pt.id as prompt_template_id,
                    pse.start_time,
                    pse.end_time
                from project_sessions ps
                join project_session_entries pse on ps.id = pse.project_session_id
                left join project_session_entry_inputs psei on pse.id = psei.project_session_entry_id
                left join project_session_entry_llm_parameters psellmp on pse.id = psellmp.project_session_entry_id 
                left join llm_model_allowed_parameters lmap on psellmp.parameter_id = lmap.id
                left join llm_models lm on lm.id = pse.model_id
                left join llm_flavors lf on lm.flavor_id = lf.id
                left join environments env on pse.environment_id = env.id
                join prompt_template_versions ptv on pse.prompt_template_version_id = ptv.id
                join prompt_templates pt on pse.prompt_template_id = pt.id
                where ps.id = :session_id
                group by ps.id, pse.id, pse.logged_at, pse.response, 
                         pse.format_type, pse.is_complete, ptv.content,
                         pt.name, pt.id, ptv.id, llm_model, llm_provider, env.name, env.is_deleted
                order by pse.logged_at
            """,
            session_id=session_id,
        )
        return try_map_details_rows_to_record(rows)

    def find_test_run_sessions_unique_providers(self, test_run_id: UUID) -> list[ProjectSessionUniqueProvidersRecord]:
        return self.db.find_all(
            type=ProjectSessionUniqueProvidersRecord,
            sql="""
                select distinct 
                    llm_models.name as llm_model_name,
                    llm_flavors.provider_name as llm_provider_name
                from project_sessions ps
                join project_session_entries pse on ps.id = pse.project_session_id
                join llm_models on llm_models.id = pse.model_id
                join llm_flavors on llm_flavors.id = llm_models.flavor_id
                where ps.test_run_id = :test_run_id
            """,
            test_run_id=test_run_id
        )

    def find_all_by_ids(self, ids: list[UUID]) -> list[ProjectSessionsRecord]:
        if len(ids) == 0:
            return []

        return self.__find_all(additional_sql_clause='where ps.id in :ids', ids=tuple(ids))

    # Aliases for multiple uses of the same table
    __last_entry = aliased(ProjectSessionEntry, name='last_entry')

    def __last_entry_subquery(self) -> ScalarSelect[UUID]:
        return sa.session.query(ProjectSessionEntry.id).filter(
            ProjectSessionEntry.project_session_id == ProjectSession.id).order_by(
            ProjectSessionEntry.logged_at.desc()).limit(1).correlate(ProjectSessionEntry).scalar_subquery()

    def create_filter_sql(self, key: str, filter: FilterConfig) -> ColumnElement[bool]:
        if key == 'response':
            return self.create_text_filter(self.__last_entry.response, filter)
        elif key == 'api_key_names':
            return self.create_text_filter(ProjectSessionEntry.api_key_name, filter)
        elif key == 'start_time':
            return self.create_date_filter(ProjectSession.start_time, filter)
        elif key == 'models':
            return self.create_set_filter(LLMModel.name, filter)
        elif key == 'prompt_names':
            return self.create_set_filter(PromptTemplate.name, filter)
        elif key == 'environments':
            return self.create_set_filter(Environment.name, filter)
        elif key == 'providers':
            return self.create_set_filter(LLMFlavor.provider_name, filter)
        elif key.startswith('inputs'):
            return self.create_inputs_filter(key, filter)
        elif key.startswith('eval_results_combined'):
            return self.create_json_filter(key, filter)
        else:
            raise FilterError(f'missing key {key}')

    def create_inputs_filter(self, key: str, filter: FilterConfig) -> ColumnElement[bool]:
        _, input_name = key.split('.', maxsplit=1)
        if filter.type == 'blank':
            return not_(exists().where(
                ProjectSessionEntry.project_session_id == ProjectSession.id,
                ProjectSessionEntryInputs.project_session_entry_id == ProjectSessionEntry.id,
                ProjectSessionEntryInputs.name == input_name,
            ).correlate(ProjectSession))
        text_filter = self.create_text_filter(ProjectSessionEntryInputs.value, filter)
        return exists().where(
            ProjectSessionEntry.project_session_id == ProjectSession.id,
            ProjectSessionEntryInputs.project_session_entry_id == ProjectSessionEntry.id,
            ProjectSessionEntryInputs.name == input_name,
            text_filter
        ).correlate(ProjectSession)

    def create_text_filter(self, col: Union[InstrumentedAttribute[str], InstrumentedAttribute[Optional[str]]],
                           filter: FilterConfig) -> ColumnElement[bool]:
        type = filter.type
        filter_value = filter.filter
        if type == 'blank':
            return or_(col == '', col == None)
        elif type == 'notBlank':
            return col != ''
        elif type == 'equals':
            return col.ilike(filter_value)
        elif type == 'notEqual':
            return col.not_ilike(filter_value)
        elif type == 'contains':
            return col.ilike(f'%{filter_value}%')
        elif type == 'notContains':
            return col.not_ilike(f'%{filter_value}%')
        elif type == 'startsWith':
            return col.ilike(f'{filter_value}%')
        elif type == 'endsWith':
            return col.ilike(f'%{filter_value}')
        else:
            raise FilterError(f'missing type {type}')

    def create_set_filter(self, col: InstrumentedAttribute[Any], filter: FilterConfig) -> ColumnElement[bool]:
        values = filter.values or []
        return col.in_(values)

    def create_date_filter(self, col: InstrumentedAttribute[datetime], filter: FilterConfig) -> ColumnElement[bool]:
        filter_date = func.to_date(filter.dateFrom, 'YYYY-MM-DD')
        target = func.date(col)

        type = filter.type
        if type == 'blank':
            return target == None
        elif type == 'notBlank':
            return target != None
        elif type == 'equals':
            return target == filter_date
        elif type == 'notEqual':
            return target != filter_date
        elif type == 'lessThan':
            return target < filter_date
        elif type == 'lessThanOrEqual':
            return target <= filter_date
        elif type == 'greaterThan':
            return target > filter_date
        elif type == 'greaterThanOrEqual':
            return target >= filter_date
        elif type == 'inRange':
            date_to = func.to_date(filter.dateTo, 'YYY-MM-DD')
            return and_(filter_date < col, col < date_to)
        else:
            raise FilterError(f'missing type {type}')

    def create_json_filter(self, key: str, filter: FilterConfig) -> ColumnElement[bool]:
        # This is a weird one because we are filtering on a JSON column that we are using as any, but the column just
        # has bare values, e.g. 1, "yes", they are not in objects or arrays.
        _, criteria_name = key.split('.', maxsplit=1)
        eval_name = EvaluationResult.criterion.has(EvaluationCriteria.name == criteria_name)
        if filter.type == 'blank':
            return not_(exists().where(
                EvaluationResult.session_id == ProjectSession.id,
                eval_name,
            ).correlate(ProjectSession))
        if filter.filterType == 'set':
            # Wrap strings in double quotes for JSON and convert to lowercase.
            string_filters = [f'"{f.lower()}"' for f in filter.values] if filter.values else []
            expression = or_(EvaluationResult.manual_score.in_(string_filters),
                             EvaluationResult.auto_eval_score.in_(string_filters))
        else:
            expression = or_(self.create_numeric_json_filter(EvaluationResult.manual_score, filter),
                             self.create_numeric_json_filter(EvaluationResult.auto_eval_score, filter))
        return exists().where(
            EvaluationResult.session_id == ProjectSession.id,
            eval_name,
            expression
        ).correlate(ProjectSession)

    def create_numeric_json_filter(self, col: InstrumentedAttribute[Any], filter: FilterConfig) -> ColumnElement[bool]:
        # Wrap in strings so that postgres can handle it as JSON.
        number = str(filter.filter)
        type = filter.type
        if type == 'notBlank':
            return col != '""'
        if type == 'equals':
            return col == number
        elif type == 'notEqual':
            return col != number
        elif type == 'lessThan':
            return col < number
        elif type == 'lessThanOrEqual':
            return col <= number
        elif type == 'greaterThan':
            return col > number
        elif type == 'greaterThanOrEqual':
            return col >= number
        elif type == 'inRange':
            return and_(number < col, col < str(filter.filterTo))
        raise ValueError('Missing filter type')

    A = TypeVar('A')

    def common_join_logic(self, select_query: Select[tuple[A]], filters: dict[str, FilterConfig]) -> Select[tuple[A]]:
        if not filters:
            return select_query

        filter_clauses = [self.create_filter_sql(key, filter_config) for key, filter_config in filters.items()]

        # We need to do the expensive joins if we are filtering.
        return (select_query
                .join(ProjectSessionEntry,
                      ProjectSession.id == ProjectSessionEntry.project_session_id)
                .outerjoin(LLMModel, ProjectSessionEntry.model_id == LLMModel.id)
                .outerjoin(LLMFlavor, LLMModel.flavor_id == LLMFlavor.id)
                .join(PromptTemplate, PromptTemplate.id == ProjectSessionEntry.prompt_template_id)
                .join(self.__last_entry, self.__last_entry.id == self.__last_entry_subquery())
                .outerjoin(Environment, Environment.id == ProjectSessionEntry.environment_id)
                .outerjoin(EvaluationResult, EvaluationResult.session_id == ProjectSession.id)
                .where(*filter_clauses)
                .distinct())

    def find_project_session_list_records(self, project_id: UUID, request: SessionsDataRequest) -> list[
        ProjectSession]:
        project_sessions_query = select(ProjectSession).where(
            ProjectSession.test_run_id.is_(None),
            ProjectSession.project_id == project_id,
            ProjectSession.start_time < request.before_datetime(),
        ).order_by(
            ProjectSession.start_time.desc()
        )

        final_query = (self.common_join_logic(project_sessions_query, request.filters)
                       .offset(request.start_row)
                       .limit(request.end_row - request.start_row))
        start_time = time.time()
        rows = sa.session.execute(final_query).scalars()
        end_time = time.time()
        logger.info(f"Session query execution time: {end_time - start_time} seconds\n%s",
                    final_query.compile(compile_kwargs={"literal_binds": True}))

        return list(rows)

    def find_prev_next_sessions(self, project_id: UUID, filters: dict[str, FilterConfig], test_run_id: Optional[UUID],
                                session_id: UUID, allowed_session_ids: Optional[list[UUID]] = None) -> tuple[
        Optional[ProjectSession], Optional[ProjectSession]]:
        current_session = sa.session.get(ProjectSession, session_id)
        if not current_session:
            raise ValueError("Missing session")
        project_sessions_query = select(ProjectSession).where(
            ProjectSession.test_run_id == test_run_id,
            ProjectSession.project_id == project_id,
        )

        if allowed_session_ids:
            project_sessions_query = project_sessions_query.where(
                ProjectSession.id.in_(allowed_session_ids)
            )

        query = self.common_join_logic(project_sessions_query, filters).limit(1)
        prev_session_query = query.where(ProjectSession.start_time > current_session.start_time).order_by(
            ProjectSession.start_time)
        next_session_query = query.where(ProjectSession.start_time < current_session.start_time).order_by(
            ProjectSession.start_time.desc())

        return (
            sa.session.execute(prev_session_query).scalar_one_or_none(),
            sa.session.execute(next_session_query).scalar_one_or_none()
        )

    def count_project_session_list_records(self, project_id: UUID, filters: dict[str, FilterConfig],
                                           before_time: datetime) -> int:
        query = select(
            func.count(distinct(ProjectSession.id))
        ).where(
            ProjectSession.project_id == project_id,
            ProjectSession.test_run_id.is_(None),
            ProjectSession.start_time < before_time,
        )
        query = self.common_join_logic(query, filters)
        return sa.session.execute(query).scalar_one()

    def delete_session(self, session_id: UUID) -> None:
        sql = """
            DELETE
            FROM
                project_sessions
            WHERE
                id = :session_id
        """
        self.db.execute(
            sql=sql,
            session_id=session_id
        )

    def exist_session_entry_in_project(self, project_id: UUID) -> bool:
        return self.db.exists(
            type=_ProjectSessionListRow,
            sql="""
                select count(1)
                from project_session_entries pse
                join prompt_templates pt on pt.id = pse.prompt_template_id
                where project_id = :project_id
            """,
            project_id=project_id,
        )

    def find_all_by_test_run(self, test_run_id: UUID) -> list[ProjectSessionsRecord]:
        additional_sql_clause = """
                WHERE ps.test_run_id = :test_run_id
        """
        return self.__find_all(additional_sql_clause=additional_sql_clause, test_run_id=test_run_id)

    def save_direct(
            self,
            connection: Connection,
            session_id: UUID,
            prompt_template_id: UUID,
            inputs: dict[Any, Any],
            llm_parameters: dict[str, Any],
            prompt_content: str,
            return_content: str,
            account_id: UUID,
            api_key_last_four: str,
            prompt_token_count: Optional[int],
            return_token_count: Optional[int],
            prompt_token_cost: Optional[Decimal],
            return_token_cost: Optional[Decimal],
            format_type: str,
            is_complete: bool,
            logged_at: datetime,
            test_run_id: Optional[UUID],
            prompt_template_version_id: Optional[UUID],  # Make this required when SDK is updated
            model: Optional[str],
            provider: Optional[str],
            start_time: datetime,
            end_time: Optional[datetime],
            function_call_response: Optional[FunctionCall],
            project_id: Optional[UUID],
            environment_id: Optional[UUID],
    ) -> ProjectSessionSavedIds:
        self.__persist_project_session_direct(
            connection,
            session_id=session_id,
            test_run_id=test_run_id,
            project_id=project_id,
            start_time=start_time,
            prompt_template_id=prompt_template_id,
        )

        db_model = self \
            .llm_models_repo \
            .try_find_model_by_provider_and_name(model, provider_name=provider) if model and provider else None

        api_key = self.api_key_repo.find_with_last(
            account_id=account_id, last=api_key_last_four
        )

        project_session_entry_id = self.__persist_project_session_entry_direct(
            connection,
            logged_at,
            session_id=session_id,
            prompt_template_id=prompt_template_id,
            prompt_content=prompt_content,
            return_content=return_content,
            prompt_token_count=prompt_token_count,
            return_token_count=return_token_count,
            prompt_token_cost=prompt_token_cost,
            return_token_cost=return_token_cost,
            format_type=format_type,
            is_complete=is_complete,
            prompt_template_version_id=prompt_template_version_id,
            model_id=db_model.id if db_model else None,
            start_time=start_time,
            end_time=end_time,
            function_call_response=function_call_response,
            api_key_last_four=api_key_last_four,
            api_key_name=api_key[0].name if len(api_key) else None,
            environment_id=environment_id,
        )

        for name in inputs:
            self.db.execute(
                sql="""
                    insert into project_session_entry_inputs (project_session_entry_id, name, value)
                    values (:project_session_entry_id, :name, :value)
                """,
                connection=connection,
                project_session_entry_id=project_session_entry_id,
                name=name,
                value=inputs[name],
            )

        if db_model:
            parameters_by_name = self.llm_models_repo.find_recordable_parameters_for_model_id(db_model.id)

            insert_values = []
            for param_name in llm_parameters:
                allowed_parameter = parameters_by_name.get(param_name)
                if allowed_parameter:
                    value = llm_parameters[param_name]
                    self.__validate_parameter_value(allowed_parameter, param_name, value)
                    if isinstance(value, dict) or isinstance(value, list):
                        value = json_support.as_str(value)

                    insert_values.append({
                        'project_session_entry_id': project_session_entry_id,
                        'parameter_id': allowed_parameter.id,
                        'value': value
                    })

            if len(insert_values) > 0:
                self.db.insert_multi(
                    sql="""
                        insert into project_session_entry_llm_parameters (project_session_entry_id, parameter_id, value)
                        values (:project_session_entry_id, :parameter_id, :value)
                    """,
                    connection=connection,
                    values=insert_values
                )

        return ProjectSessionSavedIds(session_id, project_session_entry_id)

    def __find_all(self, additional_sql_clause: str = '', **kwargs: Any) -> list[ProjectSessionsRecord]:
        rows = self.db.find_all(
            type=_ProjectSessionsRow,
            sql="""
                select
                    ps.id,
                    last_entry.logged_at, last_entry.response, first_entry.prompt_template_id,
                    last_prompt_template.project_id,
                    first_entry.prompt_template_version_id,
                    -- Use array_remove to strip [null] values from array_agg response.
                    array_remove(array_agg(inputs.name), NULL) as input_names, 
                    array_remove(array_agg(inputs.value), NULL) as input_values
                from project_sessions ps
                join project_session_entries last_entry on last_entry.id = (
                    select id from project_session_entries 
                    where project_session_id = ps.id 
                    order by logged_at desc limit 1
                )
                join project_session_entries first_entry on first_entry.id = (
                    select id from project_session_entries 
                    where project_session_id = ps.id 
                    order by logged_at limit 1
                )
                left join project_session_entry_inputs inputs on first_entry.id = inputs.project_session_entry_id
                join prompt_templates last_prompt_template on last_prompt_template.id = last_entry.prompt_template_id
                {additional_sql_clause}
                group by ps.id, last_entry.logged_at, last_entry.response, first_entry.prompt_template_id, 
                    last_prompt_template.project_id, first_entry.prompt_template_version_id
                order by last_entry.logged_at desc
            """.format(additional_sql_clause=additional_sql_clause),
            **kwargs,
        )
        return [map_list_row_to_list_record(r) for r in rows]

    def __persist_project_session_direct(
            self,
            connection: Connection,
            session_id: UUID,
            test_run_id: Optional[UUID],
            project_id: Optional[UUID],
            start_time: datetime,
            prompt_template_id: UUID,
    ) -> UUID:
        session_record_exists = self.db.exists(
            sql='select count(1) from project_sessions where id = :id',
            connection=connection,
            id=session_id
        )

        if session_record_exists:
            return session_id

        if project_id:
            return self.db.create_returning_id(
                sql="""
                insert into project_sessions (id, test_run_id, start_time, project_id)
                select :id, :test_run_id, :start_time, :project_id
                returning id
                """,
                connection=connection,
                id=session_id,
                test_run_id=test_run_id,
                start_time=start_time,
                project_id=project_id
            )

        # Remove dependency on prompt_template_id once all SDKs are sending project_id
        return self.db.create_returning_id(
            sql="""
            insert into project_sessions (id, test_run_id, start_time, project_id)
            select :id, :test_run_id, :start_time, pt.project_id
            from prompt_templates pt
            where pt.id = :prompt_template_id
            returning id
            """,
            connection=connection,
            id=session_id,
            test_run_id=test_run_id,
            start_time=start_time,
            prompt_template_id=prompt_template_id,
        )

    def __persist_project_session_entry_direct(
            self,
            connection: Connection,
            logged_at: datetime,
            session_id: UUID,
            prompt_template_id: UUID,
            prompt_content: str,
            return_content: str,
            prompt_token_count: Optional[int],
            return_token_count: Optional[int],
            prompt_token_cost: Optional[Decimal],
            return_token_cost: Optional[Decimal],
            format_type: str,
            is_complete: bool,
            prompt_template_version_id: Optional[UUID],
            model_id: Optional[UUID],
            start_time: Optional[datetime],
            end_time: Optional[datetime],
            api_key_name: Optional[str],
            api_key_last_four: Optional[str],
            environment_id: Optional[UUID],
            function_call_response: Optional[FunctionCall] = None,
    ) -> UUID:
        return self.db.create_returning_id(
            sql="""
                insert into project_session_entries (
                    logged_at,
                    project_session_id,
                    prompt_template_id,
                    prompt,
                    response,
                    prompt_token_count,
                    response_token_count,
                    prompt_token_cost,
                    response_token_cost,
                    format_type,
                    is_complete,
                    prompt_template_version_id,
                    model_id,
                    start_time,
                    end_time,
                    function_call_response,
                    api_key_last_four,
                    api_key_name,
                    environment_id
                ) values (
                    :logged_at,
                    :project_session_id,
                    :prompt_template_id,
                    :prompt_content,
                    :return_content,
                    :prompt_token_count,
                    :return_token_count,
                    :prompt_token_cost,
                    :return_token_cost,
                    :format_type,
                    :is_complete,
                    :prompt_template_version_id,
                    :model_id,
                    :start_time,
                    :end_time,
                    :function_call_response,
                    :api_key_last_four,
                    :api_key_name,
                    :environment_id
                )
                returning id
            """,
            connection=connection,
            logged_at=logged_at,
            project_session_id=session_id,
            prompt_template_id=prompt_template_id,
            prompt_content=prompt_content,
            return_content=return_content,
            prompt_token_count=prompt_token_count,
            return_token_count=return_token_count,
            prompt_token_cost=prompt_token_cost,
            return_token_cost=return_token_cost,
            format_type=format_type,
            is_complete=is_complete,
            prompt_template_version_id=prompt_template_version_id,
            model_id=model_id,
            start_time=start_time,
            end_time=end_time,
            function_call_response=json_support.as_str(function_call_response),
            api_key_last_four=api_key_last_four,
            api_key_name=api_key_name,
            environment_id=environment_id
        )

    @staticmethod
    def __validate_parameter_value(allowed_parameter: LLMAllowedParameter, param_name: str, value: Any) -> None:
        if allowed_parameter.parameter_type == LLMModelParameterType.Integer:
            try:
                int(value)
            except ValueError:
                raise UnexpectedParameterError(f'Invalid value passed for LLM parameter {param_name}')
        if allowed_parameter.parameter_type == LLMModelParameterType.Float:
            try:
                float(value)
            except ValueError:
                raise UnexpectedParameterError(f'Invalid value passed for LLM parameter {param_name}')
