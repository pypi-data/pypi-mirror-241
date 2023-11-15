import uuid
from dataclasses import dataclass
from uuid import UUID


@dataclass
class ProjectSession:
    session_id: UUID


class ProjectSessionCreator:

    def create(self) -> ProjectSession:
        return ProjectSession(
            session_id=uuid.uuid4(),
        )
