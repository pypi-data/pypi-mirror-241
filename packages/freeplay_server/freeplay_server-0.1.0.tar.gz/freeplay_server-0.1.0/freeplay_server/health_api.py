from flask import Blueprint, jsonify
from flask.typing import ResponseReturnValue

from freeplay_server.auth.auth_filter import public_endpoint
from freeplay_server.database_support.database_gateway import DatabaseGateway


def health_api(db: DatabaseGateway) -> Blueprint:
    api = Blueprint('health_api', __name__)

    def __check_db_connection() -> bool:
        try:
            db.query('select 1')
            return True
        except:
            return False

    @public_endpoint
    @api.get('/health')
    def health() -> ResponseReturnValue:
        if not __check_db_connection():
            return jsonify({'status': 'DOWN', 'message': 'failure to connect to database'}), 503

        return jsonify({'status': 'UP'})

    return api
