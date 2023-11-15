from typing import Optional, Any

from flask import Blueprint, g, jsonify
from flask.typing import ResponseReturnValue

from freeplay_server.auth.auth_filter import api_endpoint
from freeplay_server.project_sessions.project_session_creator import ProjectSessionCreator
from freeplay_server.projects.projects_repository import ProjectsRepository
from freeplay_server.web_support.api_support import try_parse_uuid, api_not_found


def project_sessions_api(
        projects_repo: ProjectsRepository,
        session_creator: ProjectSessionCreator = ProjectSessionCreator()
) -> Blueprint:
    api = Blueprint('project_sessions_api', __name__, url_prefix='/api/projects/<project_id>/sessions')

    @api.url_value_preprocessor
    def extract_project_id(_: Optional[str], values: Optional[dict[str, Any]]) -> None:
        values = values or {}
        maybe_project_id = values.pop('project_id', None)

        if maybe_project_id is None:
            return

        project_id = try_parse_uuid(maybe_project_id)
        if project_id is None:
            return

        g.project = projects_repo.try_find(project_id)

    @api.before_request
    def before_request() -> Optional[ResponseReturnValue]:
        if g.project is None:
            return api_not_found('Project not found')

        return None

    @api_endpoint
    @api.post('/tag/<tag>')
    def create_by_tag(tag: str) -> ResponseReturnValue:
        session = session_creator.create()
        return jsonify(session), 201

    return api
