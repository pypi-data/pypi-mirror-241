from dataclasses import dataclass
from enum import Enum
from typing import List, Optional
from uuid import UUID

from sqlalchemy import Connection

from freeplay_server.database_support.database_gateway import DatabaseGateway


class ProjectPersistenceFailure(Enum):
    NameAlreadyTaken = 'This name is already taken'


@dataclass
class ProjectRecord:
    id: UUID
    name: str


@dataclass(frozen=True)
class Tag:
    tag: str

    
class ProjectsRepository:

    def __init__(self, db: DatabaseGateway) -> None:
        self.db = db

    def try_find(self, project_id: UUID) -> Optional[ProjectRecord]:
        return self.db.try_find(
            type=ProjectRecord,
            sql="select id, name from projects where id = :id",
            id=project_id
        )

    def find_all(self) -> List[ProjectRecord]:
        return self.db.find_all(
            type=ProjectRecord,
            sql="select id, name from projects order by name"
        )

    def delete(self, id: UUID) -> None:
        self.db.execute(
            sql='delete from projects where id = :id',
            id=id
        )
