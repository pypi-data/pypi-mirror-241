import re
import typing as t

import dacite
from flask import request

from freeplay_server.web_support.json_support import dacite_config

T = t.TypeVar("T")


def __extract_prefixed_fields(prefix: str, all_values: dict[str, str]) -> dict[str, t.Any]:
    field_values: dict[str, t.Any] = {}

    for key in all_values:
        if key.startswith(prefix):
            new_key = key.removeprefix(prefix).removeprefix('[').removesuffix(']')
            field_values[new_key] = all_values[key]

    return field_values


def __try_find_max_index(prefix: str, all_values: dict[str, str]) -> t.Optional[int]:
    regexp = r"" + prefix + "\\[([0-9]+)\\]"
    max_index = -1

    for field_name in all_values:
        try:
            match = re.search(regexp, field_name)
            if match is not None:
                current_index = int(match.group(1))
                max_index = max(current_index, max_index)
        except:
            pass

    if max_index == -1:
        return None

    return max_index


def try_decode_form(
    target_type: t.Type[T],
    get_form_data: t.Callable[[], dict[str, str]] = lambda: request.form.to_dict()
) -> t.Optional[T]:
    try:
        return dacite.from_dict(target_type, get_form_data(), config=dacite_config())
    except:
        return None


def strip_empty_form_values() -> dict[str, str]:
    output = {}
    for (k, v) in request.form.items():
        if v != "":
            output[k] = v

    return output


def decode_form_list(
    target_type: t.Type[T],
    prefix: str,
    get_form_data: t.Callable[[], dict[str, str]] = lambda: request.form.to_dict()
) -> t.Optional[list[T]]:
    form_list: list[T] = []
    form_data = get_form_data()
    max_index = __try_find_max_index(prefix, form_data)

    if max_index is None:
        return []

    for index in range(0, max_index + 1):
        index_prefix = f"{prefix}[{index}]"
        fields = __extract_prefixed_fields(index_prefix, form_data)
        try:
            decoded = dacite.from_dict(target_type, fields, config=dacite_config())
            form_list.append(decoded)
        except:
            return None

    return form_list
