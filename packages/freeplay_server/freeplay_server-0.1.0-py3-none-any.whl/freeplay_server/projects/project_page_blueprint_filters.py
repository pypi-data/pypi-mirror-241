from typing import Optional, Any, Callable
from uuid import UUID

from flask import g, abort
from flask.typing import ResponseReturnValue

from freeplay_server.projects.projects_repository import ProjectRecord
from freeplay_server.web_support.api_support import try_parse_uuid, api_not_found

ProjectFinder = Callable[[UUID], Optional[ProjectRecord]]
AllProjectFinder = Callable[[], list[ProjectRecord]]


class ProjectPageBlueprintFilters:

    def __init__(
            self,
            project_finder: ProjectFinder,
            all_project_finder: AllProjectFinder,
    ):
        self.project_finder = project_finder
        self.all_project_finder = all_project_finder

    def hydrate_projects(self, values: Optional[dict[str, Any]]) -> None:
        values = values or {}
        maybe_project_id = values.pop('project_id', None)

        if maybe_project_id is not None:
            project_id = try_parse_uuid(maybe_project_id)

            if project_id is not None:
                g.project = self.project_finder(project_id)

        g.all_projects = self.all_project_finder()

    @staticmethod
    def before_api_request() -> Optional[ResponseReturnValue]:
        if g.get('project', None) is None:
            return api_not_found('Project not found')

        return None

    @staticmethod
    def before_page_request() -> Optional[ResponseReturnValue]:
        if g.get('project', None) is None:
            abort(404)

        return None
