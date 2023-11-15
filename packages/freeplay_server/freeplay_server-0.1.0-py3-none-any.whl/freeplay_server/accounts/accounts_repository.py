import uuid
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional, Union
from uuid import UUID

from sqlalchemy.engine import Connection

from freeplay_server.accounts.users import Roles
from freeplay_server.database_support.database_gateway import DatabaseGateway

DEFAULT_ACCOUNT_NAME = 'Default Account'


class AccountPersistenceFailure(Enum):
    NameAlreadyTaken = 'This name is already taken'


class UserPersistenceFailure(Enum):
    NameAlreadyTaken = 'This email address is already taken'
    RoleNotFound = 'The role for this user was not found'
    UserNotFound = 'User not found'


@dataclass
class AccountRecord:
    id: UUID
    name: str
    tos_accepted_date: Optional[datetime]
    tos_accepted_user_email: Optional[str]


@dataclass
class UserRecord:
    id: UUID
    first_name: str
    last_name: str
    email_address: str
    stytch_user_id: str
    is_internal: Optional[bool]


@dataclass
class UserWithRoleRecord:
    id: UUID
    first_name: Optional[str]
    last_name: Optional[str]
    email_address: str
    role_name: str


@dataclass
class UserWithRoleAndObfuscatedEmailRecord(UserWithRoleRecord):
    def __init__(self, id: UUID, first_name: Optional[str], last_name: Optional[str], email_address: str,
                 role_name: str) -> None:

        super().__init__(id, first_name, last_name, email_address, role_name)
        parts = email_address.split("@")
        if len(parts) == 2:
            username, domain = parts
            obfuscated_email = username[:2] + "***@" + domain
            self.email_address = obfuscated_email
        else:
            self.email_address = ""


@dataclass
class RoleRecord:
    id: UUID
    name: str


AccountCreationResult = Union[
    AccountRecord,
    AccountPersistenceFailure,
]

UserCreationResult = Union[
    UserRecord,
    UserPersistenceFailure,
]

UserEditResult = Optional[UserPersistenceFailure]


class AccountsRepository:

    def __init__(self, db: DatabaseGateway) -> None:
        self.db = db

    def try_find(self, account_id: UUID) -> Optional[AccountRecord]:
        return self.db.try_find(
            type=AccountRecord,
            sql="select id, name, tos_accepted_date from accounts where id = :id",
            id=account_id
        )

    def try_find_by_name(self, account_name: str) -> Optional[AccountRecord]:
        return self.db.try_find(
            type=AccountRecord,
            sql="select id, name, tos_accepted_date from accounts where name = :name",
            name=account_name
        )

    def find_all(self) -> List[AccountRecord]:
        return self.db.find_all(
            type=AccountRecord,
            sql="select id, name from accounts"
        )

    def find_all_users(self, account_id: UUID) -> List[UserRecord]:
        return self.db.find_all(
            type=UserRecord,
            sql="""select u.id, email_address, stytch_user_id
                   from users u join users_accounts ua on u.id=ua.user_id 
                   where account_id = :account_id""",
            account_id=account_id
        )

    def find_all_users_with_role(self, account_id: UUID, logged_in_user_email: str, is_admin_role: bool = False) \
            -> List[UserWithRoleRecord | UserWithRoleAndObfuscatedEmailRecord]:
        user = self.find_user_by_email_address(logged_in_user_email)
        is_internal = user.is_internal if user is not None else False

        query = """
            SELECT u.id, u.first_name, u.last_name, u.email_address, u.stytch_user_id, r.name as role_name 
            FROM users u 
            JOIN users_accounts ua ON u.id = ua.user_id 
            JOIN user_account_roles uar ON uar.user_account_id = ua.id 
            JOIN roles r ON r.id = uar.role_id
            WHERE ua.account_id = :account_id
        """

        if not is_internal:
            query += " AND u.is_internal != true"

        query += " ORDER BY r.name ASC, u.first_name ASC"

        results = self.db.find_all(
            type=UserWithRoleRecord if is_admin_role else UserWithRoleAndObfuscatedEmailRecord,
            sql=query,
            account_id=account_id)
        return results

    def create_account(self, name: str) -> AccountCreationResult:
        with self.db.transaction() as connection:
            name_exists = self.db.exists(
                'select count(id) from accounts where name = :name',
                connection,
                name=name,
            )

            if name_exists:
                return AccountPersistenceFailure.NameAlreadyTaken

            new_id = uuid.uuid4()
            account_id = self.db.create_returning_id("""
                insert into accounts (id, name) values (:account_id, :name) returning id
                """, connection, account_id=new_id, name=name)

            return AccountRecord(account_id, name, None, None)

    def create_user(
            self,
            first_name: str,
            last_name: str,
            email_address: str,
            account_id: UUID,
            stytch_user_id: str,
            is_internal: bool = False,
            is_admin_user: bool = False,
    ) -> UserCreationResult:
        with self.db.transaction() as connection:
            name_exists = self.db.exists(
                'select count(id) from users where email_address = :email_address',
                connection,
                email_address=email_address,
            )
            if name_exists:
                return UserPersistenceFailure.NameAlreadyTaken

            user_id = self.__insert_user(connection, email_address, first_name, last_name, stytch_user_id, is_internal)
            membership_id = self.__insert_account_membership(connection, account_id, user_id)

            role_result = self.__insert_role(connection, membership_id, is_admin_user)
            if not role_result:
                return UserPersistenceFailure.RoleNotFound

            return UserRecord(user_id, first_name, last_name, email_address, stytch_user_id, is_internal=is_internal)

    def find_user_by_stytch_user_id(self, stytch_user_id: str) -> Optional[UserRecord]:
        return self.db.try_find(
            type=UserRecord,
            sql="select id, first_name, last_name, email_address, stytch_user_id, is_internal from users u where stytch_user_id = :stytch_user_id",
            stytch_user_id=stytch_user_id
        )

    def find_user_by_email_address(self, user_email_address: str) -> Optional[UserRecord]:
        return self.db.try_find(
            type=UserRecord,
            sql="select id, first_name, last_name, email_address, stytch_user_id, is_internal from users u where email_address = :email_address",
            email_address=user_email_address
        )

    def should_accept_tos(self, logged_in_user_email: str) -> bool:
        account = self.try_find_by_name(DEFAULT_ACCOUNT_NAME)

        if account and account.tos_accepted_date is None:
            user = self.find_user_by_email_address(logged_in_user_email)
            is_internal = user.is_internal if user is not None else False
            return not is_internal

        return False

    def accept_account_tos(self, account_id: UUID, user_email: str) -> None:
        with self.db.transaction() as connection:
            self.db.execute(
                sql="""
                    UPDATE accounts
                    SET  tos_accepted_user_email = :user_email,
                    tos_accepted_date = NOW()
                    WHERE id = :account_id
                """,
                user_email=user_email,
                account_id=account_id
            )

    def __insert_user(
            self,
            connection: Connection,
            email_address: str,
            first_name: str,
            last_name: str,
            stytch_user_id: str,
            is_internal: bool = False
    ) -> UUID:
        user_id = self.db.create_returning_id(
            """
                insert into users (id, email_address, first_name, last_name, stytch_user_id, is_internal)
                values (:id, :email_address, :first_name, :last_name, :stytch_user_id, :is_internal) returning id
                """,
            connection,
            id=uuid.uuid4(),
            email_address=email_address,
            first_name=first_name,
            last_name=last_name,
            stytch_user_id=stytch_user_id,
            is_internal=is_internal
        )
        return user_id

    def __insert_account_membership(self, connection: Connection, account_id: UUID, user_id: UUID) -> UUID:
        membership_id = self.db.create_returning_id("""
                insert into users_accounts (user_id, account_id) 
                values(:user_id, :account_id) returning id
                """, connection, user_id=user_id, account_id=account_id)
        return membership_id

    def __find_account_membership(self, connection: Connection, user_id: UUID) -> UUID | None:
        membership_id = self.db.try_find_id("""
            SELECT id FROM users_accounts WHERE user_id = :user_id
         """, connection, user_id=user_id)

        return membership_id

    def __insert_role(self, connection: Connection, membership_id: UUID, is_admin_user: bool) -> bool:
        role_name = Roles.ACCOUNT_USER
        if is_admin_user:
            role_name = Roles.ACCOUNT_ADMIN

        roles = self.db.find_all(
            type=RoleRecord,
            sql='select id, name from roles where name=:role_name',
            role_name=role_name.value)

        if len(roles) != 1:
            return False

        self.db.execute(
            """insert into user_account_roles (user_account_id, role_id)
            values (:user_account_id, :role_id)""",
            connection=connection,
            user_account_id=membership_id,
            role_id=roles[0].id
        )

        return True

    def __edit_role(self, connection: Connection, membership_id: UUID, is_admin_user: bool) -> bool:
        role_name = Roles.ACCOUNT_ADMIN if is_admin_user else Roles.ACCOUNT_USER

        role = self.db.try_find(
            type=RoleRecord,
            sql='select id, name from roles where name=:role_name',
            role_name=role_name.value)

        if not role:
            return False

        self.db.execute(
            """
                UPDATE user_account_roles 
                SET role_id=:role_id
                WHERE user_account_id=:user_account_id
            """,
            connection=connection,
            user_account_id=membership_id,
            role_id=role.id
        )

        return True

    def edit_user(
            self,
            user_id: UUID,
            first_name: str,
            last_name: str,
            is_admin_user: bool = False,
    ) -> UserEditResult:
        with self.db.transaction() as connection:
            if not user_id:
                return UserPersistenceFailure.UserNotFound

            self.db.execute(
                sql="""
                    UPDATE users
                    SET 
                        first_name = :first_name,
                        last_name = :last_name
                    WHERE id = :user_id
                """,
                connection=connection,
                first_name=first_name,
                last_name=last_name,
                user_id=user_id,
            )

            membership_id = self.__find_account_membership(connection, user_id)
            if not membership_id:
                return UserPersistenceFailure.UserNotFound

            role_result = self.__edit_role(connection, membership_id, is_admin_user)
            if not role_result:
                return UserPersistenceFailure.RoleNotFound

            return None
