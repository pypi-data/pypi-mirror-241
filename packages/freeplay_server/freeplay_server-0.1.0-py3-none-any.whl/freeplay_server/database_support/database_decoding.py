from typing import TypeVar, Type, Mapping, Any, cast
from uuid import UUID

import dacite
from sqlalchemy import RowMapping
from sqlalchemy.engine import Row, CursorResult

from freeplay_server.web_support import json_support

T = TypeVar("T")


def decode_row(target_type: Type[T], row: RowMapping) -> T:
    return dacite.from_dict(target_type, dict(row), config=json_support.dacite_config())


def extract_prefixed_fields(prefix: str, row: Row[Any]) -> Mapping[str, Any]:
    values: dict[str, Any] = {}
    mapping = row._mapping

    for key in mapping.keys():
        if key.startswith(prefix):
            values[key.removeprefix(prefix)] = mapping[key]

    return values


def decode_single_row(target_type: Type[T], res: CursorResult[Any]) -> T:
    count = res.rowcount
    if count != 1:
        raise Exception('Expected single row result')

    for row in res:
        return decode_row(target_type, row._mapping)

    raise Exception('Expected single row result')


def decode_single_id(res: CursorResult[Any]) -> UUID:
    count = res.rowcount
    if count != 1:
        raise Exception('Expected single row result')

    for row in res:
        return cast(UUID, row.id)

    raise Exception('Expected single row result')
