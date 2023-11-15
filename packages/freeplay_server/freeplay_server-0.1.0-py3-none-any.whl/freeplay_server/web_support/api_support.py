from typing import Optional
from uuid import UUID

from flask import jsonify
from flask.typing import ResponseReturnValue


def api_bad_request(message: str) -> ResponseReturnValue:
    return jsonify({'message': message}), 400


def api_not_found(message: str) -> ResponseReturnValue:
    return jsonify({'message': message}), 404


def try_parse_uuid(uuid_as_string: str) -> Optional[UUID]:
    try:
        return UUID(hex=uuid_as_string)
    except:
        return None
