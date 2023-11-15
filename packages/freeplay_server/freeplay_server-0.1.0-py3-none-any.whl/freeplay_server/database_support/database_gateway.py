from typing import Type, Any, Optional, TypeVar, cast
from uuid import UUID

import sqlalchemy
from sqlalchemy.engine import CursorResult, Connection

from freeplay_server.database_support.database_decoding import decode_row, decode_single_row, decode_single_id

T = TypeVar("T")


def count(res: CursorResult[Any]) -> int:
    # noinspection PyTypeChecker
    return res.rowcount


def try_decode_single_row(target_type: Type[T], res: CursorResult[Any]) -> Optional[T]:
    if count(res) != 1:
        return None

    for row in res:
        return decode_row(target_type, row._mapping)

    return None


def decode_all_rows(target_type: Type[T], res: CursorResult[Any]) -> list[T]:
    return [
        decode_row(target_type, row._mapping)
        for row in res
    ]


def decode_all_ids(res: CursorResult[Any]) -> list[UUID]:
    return [
        cast(UUID, row.id)
        for row in res
    ]


class DatabaseGateway:

    def __init__(self, engine: sqlalchemy.Engine) -> None:
        self.__engine = engine

    def dispose(self) -> None:
        if self.__engine:
            self.__engine.dispose()

    def transaction(self) -> Connection:
        return cast(Connection, self.__engine.begin())

    def query(self, sql: str, connection: Optional[Connection] = None, **kwargs: Any) -> CursorResult[Any]:
        if connection is None:
            with self.__engine.begin() as connection:
                return connection.execute(sqlalchemy.text(sql), kwargs)
        else:
            return connection.execute(sqlalchemy.text(sql), kwargs)

    def execute(self, sql: str, connection: Optional[Connection] = None, **kwargs: Any) -> None:
        self.query(sql, connection, **kwargs)

    def execute_return_count(self, sql: str, connection: Optional[Connection] = None, **kwargs: Any) -> int:
        query = self.query(sql, connection, **kwargs)
        # noinspection PyTypeChecker
        return query.rowcount

    def insert_multi(self, sql: str, connection: Optional[Connection], values: list[dict[str, Any]]) -> None:
        if connection is None:
            with self.__engine.begin() as connection:
                connection.execute(sqlalchemy.text(sql), parameters=values)
        else:
            connection.execute(sqlalchemy.text(sql), parameters=values)

    def create(self, type: Type[T], sql: str, connection: Optional[Connection] = None, **kwargs: Any) -> T:
        result = self.query(sql, connection, **kwargs)
        return decode_single_row(type, result)

    def create_returning_id(self, sql: str, connection: Optional[Connection] = None, **kwargs: Any) -> UUID:
        result = self.query(sql, connection, **kwargs)
        return decode_single_id(result)

    def find_all(self, type: Type[T], sql: str, connection: Optional[Connection] = None, **kwargs: Any) -> list[T]:
        result = self.query(sql, connection, **kwargs)
        return decode_all_rows(type, result)

    def find_all_ids(self, sql: str, connection: Optional[Connection] = None, **kwargs: Any) -> list[UUID]:
        result = self.query(sql, connection, **kwargs)
        return decode_all_ids(result)

    def try_find(self, type: Type[T], sql: str, connection: Optional[Connection] = None, **kwargs: Any) -> Optional[T]:
        result = self.query(sql, connection, **kwargs)
        return try_decode_single_row(type, result)

    def try_find_id(self, sql: str, connection: Optional[Connection] = None, **kwargs: Any) -> Optional[UUID]:
        result = self.query(sql, connection, **kwargs)

        if count(result) == 0:
            return None

        return decode_single_id(result)

    def update(self, type: Type[T], sql: str, connection: Optional[Connection], **kwargs: Any) -> Optional[T]:
        result = self.query(sql, connection, **kwargs)
        return try_decode_single_row(type, result)

    def count(self, sql: str, connection: Optional[Connection] = None, **kwargs: Any) -> int:
        result = self.query(sql, connection, **kwargs)

        if count(result) != 1:
            raise Exception('Count expects a SQL query for a count, e.g. select count(id) from foo')

        for r in result:
            return int(r[0])

        raise Exception('Count expects a SQL query for a count, e.g. select count(id) from foo')

    def exists(self, sql: str, connection: Optional[Connection] = None, **kwargs: Any) -> bool:
        return self.count(sql, connection, **kwargs) > 0
