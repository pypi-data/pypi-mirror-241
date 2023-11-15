import uuid
from dataclasses import dataclass
from enum import Enum


class Roles(Enum):
    ACCOUNT_USER = "Account User"
    ACCOUNT_ADMIN = "Account Admin"

    @staticmethod
    def from_str(str: str) -> "Roles":
        for role in Roles:
            if role.value == str:
                return role
        raise ValueError(f'Invalid value for Roles: {str}')


@dataclass
class SessionUser:
    id: uuid.UUID
    first_name: str
    last_name: str
    email_address: str
    roles: list[Roles]

    def is_admin(self) -> bool:
        return Roles.ACCOUNT_ADMIN in self.roles

