import dataclasses
import json
import logging
import typing as t
from enum import Enum
from uuid import UUID

import dacite

from freeplay_server.utilities.encoding_utils import CharacterEncoding

logger = logging.getLogger(__name__)


class EncoderWithDataClassSupport(json.JSONEncoder):
    def default(self, o: t.Any) -> t.Any:
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        if type(o) is UUID:
            return str(o)

        return super().default(o)


T = t.TypeVar("T")


def decode_uuid(value: t.Any) -> t.Any:
    if type(value) is UUID:
        return value

    if type(value) is str:
        return UUID(hex=value)

    raise Exception(f'Failed to decode UUID from value {value}')


def dacite_config() -> dacite.Config:
    return dacite.Config(type_hooks={UUID: decode_uuid}, cast=[Enum])


def force_decode(target_type: t.Type[T], data: bytes) -> T:
    parsed_json = json.loads(data)
    return __map_to_type(parsed_json, target_type)


def force_decode_list(target_type: t.Type[T], data: bytes) -> list[T]:
    json_list = json.loads(data)
    if not isinstance(json_list, list):
        raise Exception('Unable to decode json because it was not a list')

    return [
        dacite.from_dict(target_type, list_item, config=dacite_config())
        for list_item in json_list
    ]

def force_decode_dict(target_type: t.Type[T], data: bytes) -> dict[str, T]:
    json_dict = json.loads(data)
    if not isinstance(json_dict, dict):
        raise Exception('Unable to decode json because it was not a list')

    return {key:
        dacite.from_dict(target_type, value, config=dacite_config())
        for (key, value) in json_dict.items()
    }


def force_decode_str(target_type: t.Type[T], data: str) -> T:
    return force_decode(target_type, data.encode(CharacterEncoding.UTF_8))


def try_decode(target_type: t.Type[T], data: bytes) -> t.Optional[T]:
    try:
        return force_decode(target_type, data)
    except Exception as e:
        logger.error(f'There was an error decoding the json, {e}')
        return None


def try_decode_list(target_type: t.Type[T], data: bytes) -> t.Optional[list[T]]:
    try:
        return force_decode_list(target_type, data)
    except Exception as e:
        logger.debug(f'There was an error decoding the json, {e}')
        return None


def try_decode_str(target_type: t.Type[T], data: str) -> t.Optional[T]:
    return try_decode(target_type, data.encode(CharacterEncoding.UTF_8))


def try_decode_str_include_dom(
        target_type: t.Type[T],
        data: str
) -> t.Tuple[t.Optional[T], dict[t.Any, t.Any]]:
    dom = json.loads(data.encode(CharacterEncoding.UTF_8))
    try:
        return __map_to_type(dom, target_type), dom
    except Exception as e:
        logger.error(f'There was an error decoding the json, {e}')
        return None, dom


def encode(obj: t.Any) -> bytes:
    return json \
        .dumps(obj, cls=EncoderWithDataClassSupport) \
        .encode(encoding=CharacterEncoding.UTF_8)


def as_str(obj: t.Any) -> str:
    return json.dumps(obj, cls=EncoderWithDataClassSupport)


def as_json(obj: t.Any) -> dict[t.Any, t.Any]:
    return t.cast(dict[t.Any, t.Any], json.loads(encode(obj)))


def as_dict(json_str: str) -> dict[t.Any, t.Any]:
    return t.cast(dict[t.Any, t.Any], json.loads(json_str))


def __map_to_type(parsed_json: dict[t.Any, t.Any], target_type: t.Type[T]) -> T:
    return dacite.from_dict(target_type, parsed_json, config=dacite_config())
