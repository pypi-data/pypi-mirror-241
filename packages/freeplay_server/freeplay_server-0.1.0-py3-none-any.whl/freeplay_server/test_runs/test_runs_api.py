from dataclasses import dataclass
from typing import Optional, Any

from flask import Blueprint, request, g, jsonify
from flask.typing import ResponseReturnValue

from freeplay_server.auth.auth_filter import api_endpoint
from freeplay_server.test_lists.test_lists_repository import TestListsRepository
from freeplay_server.projects.project_page_blueprint_filters import ProjectPageBlueprintFilters
from freeplay_server.test_runs.test_runs_service import TestRunsService, TestRunWithSubjects
from freeplay_server.web_support.api_support import api_bad_request, api_not_found


@dataclass
class TestRunInfo:
    test_run_id: str
    inputs: list[dict[str, str]]

    def __init__(self, test_run: TestRunWithSubjects) -> None:
        self.test_run_id = str(test_run.id)
        self.inputs = [s.inputs for s in test_run.subjects]


def build_test_runs_api(
        filters: ProjectPageBlueprintFilters,
        test_list_repo: TestListsRepository,
        test_runs: TestRunsService) -> Blueprint:
    api = Blueprint('test_runs_api', __name__, url_prefix='/api/projects/<project_id>/test-runs')

    @api.url_value_preprocessor
    def hydrate_projects(_: Optional[str], values: Optional[dict[str, Any]]) -> None:
        filters.hydrate_projects(values)

    @api.before_request
    def before_request() -> Optional[ResponseReturnValue]:
        return filters.before_api_request()

    @api_endpoint
    @api.post('')
    def create() -> ResponseReturnValue:
        # Intentionally uses playlist_name for backwards compatibility with existing SDK versions
        playlist_name = request.get_json().get('playlist_name', None)
        if playlist_name is None:
            return api_bad_request('Missing playlist_name in json payload')

        test_list = test_list_repo.try_find_by_project_id_and_name(g.project.id, playlist_name)
        if test_list is None:
            return api_not_found('Playlist not found')

        test_run = test_runs.create(test_list)

        return jsonify(TestRunInfo(test_run)), 201

    return api
