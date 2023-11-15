from dataclasses import dataclass
from datetime import date
from typing import List, Optional
from uuid import UUID

from sqlalchemy import Connection

from freeplay_server.database_support.database_gateway import DatabaseGateway


@dataclass(frozen=True)
class EnvironmentType:
    id: UUID
    name: str
    created_date: date
    is_deleted: bool

@dataclass(frozen=True)
class ModelsType:
    id: UUID
    display_name: str
    name: str
    is_active: bool
    provider_name: Optional[str] = None
    flavor_type: Optional[str] = None
    is_default: Optional[bool] = False


@dataclass(frozen=True)
class AzureModels:
    id: UUID
    name: str


@dataclass(frozen=True)
class AzureEndpointType:
    id: UUID
    name: str
    deployment_id: str
    api_version: str
    model_id: UUID
    is_active: bool


@dataclass(frozen=True)
class AzureNewEndpointType:
    name: str
    deployment_id: str
    api_version: str
    model_id: UUID
    is_active: bool


class EnvironmentsRepository:

    def __init__(self, db: DatabaseGateway) -> None:
        self.db = db

    def try_find(self, environment_id: UUID) -> Optional[EnvironmentType]:
        return self.db.try_find(
            type=EnvironmentType,
            sql="""
                SELECT id, name, created_date, is_deleted
                FROM environments
                WHERE id = :environment_id
            """,
            environment_id=environment_id
        )

    def try_find_by_name(self, name: str, connection: Optional[Connection] = None) -> Optional[EnvironmentType]:
        return self.db.try_find(
            type=EnvironmentType,
            sql="""
                SELECT id, name, created_date, is_deleted
                FROM environments
                WHERE name = :name
            """,
            name=name,
            connection=connection
        )

    def find_all(self) -> List[EnvironmentType]:
        return self.db.find_all(
            type=EnvironmentType,
            sql="""
                SELECT id, name, created_date, is_deleted
                FROM environments
                WHERE is_deleted = False
                ORDER BY name
            """
        )

    def create_environment(self, name: str, connection: Optional[Connection] = None) -> UUID:
        return self.db.create_returning_id(
            sql="""
                INSERT INTO environments (name)
                VALUES (:name) RETURNING id
            """,
            name=name,
            connection=connection
        )

    def check_and_create_environment(self, name: str, connection: Optional[Connection] = None) -> str:
        env = self.try_find_by_name(name, connection)
        if not env:
            return str(self.create_environment(name, connection))
        else:
            return str(env.id)

    def update_environment_name(self, environment_id: UUID, name: str) -> None:
        self.db.execute(
            sql="""
                UPDATE environments
                SET name = :name
                WHERE id = :environment_id
            """,
            name=name,
            environment_id=environment_id
        )

    def soft_delete_environment(self, environment_id: UUID) -> None:
        self.db.execute(
            sql="""
                UPDATE environments
                SET is_deleted = true
                WHERE id = :environment_id
            """,
            environment_id=environment_id
        )

class ModelsRepository:
    def __init__(self, db: DatabaseGateway) -> None:
        self.db = db

    def find_all(self) -> List[ModelsType]:
        return self.db.find_all(
            type=ModelsType,
            sql="""
                SELECT id, display_name, name, is_active
                FROM llm_flavors
                ORDER BY name
            """
        )

    def find_default_models(self) -> List[ModelsType]:
        return self.db.find_all(
            type=ModelsType,
            sql="""
                SELECT
                    id,
                    display_name,
                    provider_name,
                    name,
                    is_active,
                    is_default
                FROM
                    llm_flavors llf
                WHERE
                    llf.is_default
            """
        )

    def find_non_default_models(
        self,
        filter_by_provider: Optional[tuple[str]] = None
    ) -> List[AzureModels]:
        base_sql = """
            SELECT
                lm.id as id,
                lm.name as name
            FROM llm_models lm
            JOIN llm_flavors lf ON lm.flavor_id = lf.id
        """
        join_query = """
            WHERE lf.provider_name in :providers_list
            AND lf.is_default = false
        """
        if filter_by_provider:
            base_sql += join_query
        else:
            base_sql += "WHERE lf.is_default = false"

        return self.db.find_all(
            type=AzureModels,
            sql=base_sql,
            providers_list=filter_by_provider
        )

    def update_models(self, model: ModelsType) -> None:
        self.db.execute(
            sql="""
                UPDATE llm_flavors
                SET
                    is_active = :is_active
                WHERE id = :model_id
            """,
            is_active=model.is_active,
            model_id=model.id
        )

    def find_all_azure_endpoints(self, account_id: UUID) -> List[AzureEndpointType]:
        return self.db.find_all(
            type=AzureEndpointType,
            sql="""
                SELECT id, is_active, name, deployment_id, api_version, model_id
                FROM endpoint_model_configs
                WHERE account_id = :account_id
            """,
            account_id=account_id
        )

    def create_azure_endpoint(self, endpoint: AzureNewEndpointType, account_id: UUID) -> None:
        self.db.execute(
            type=AzureNewEndpointType,
            sql="""
                INSERT
                    INTO endpoint_model_configs (
                        is_active, name, deployment_id, api_version, model_id, account_id
                    )
                    VALUES (
                        :is_active, :name, :deployment_id, :api_version, :model_id, :account_id
                    )
            """,
            is_active=endpoint.is_active,
            name=endpoint.name,
            deployment_id=endpoint.deployment_id,
            api_version=endpoint.api_version,
            model_id=endpoint.model_id,
            account_id=account_id,
        )

    def update_azure_endpoint(self, endpoint: AzureEndpointType, account_id: UUID) -> None:
        self.db.execute(
            type=AzureEndpointType,
            sql="""
                UPDATE endpoint_model_configs
                SET
                    is_active = :is_active,
                    name = :name,
                    deployment_id = :deployment_id,
                    api_version = :api_version,
                    model_id = :model_id
                WHERE id = :id
                AND account_id=:account_id
            """,
            is_active=endpoint.is_active,
            name=endpoint.name,
            deployment_id=endpoint.deployment_id,
            api_version=endpoint.api_version,
            model_id=endpoint.model_id,
            id=endpoint.id,
            account_id=account_id,
        )

    def delete_endpoint(self, endpoint_id: UUID, account_id: UUID) -> None:
        self.db.execute(
            sql="""
                DELETE FROM endpoint_model_configs
                WHERE id = :endpoint_id
                AND account_id=:account_id
            """,
            endpoint_id=endpoint_id,
            account_id=account_id
        )
