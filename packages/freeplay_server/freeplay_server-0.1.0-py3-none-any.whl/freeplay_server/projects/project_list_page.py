from typing import Optional, cast, Any
from uuid import UUID

from flask import Blueprint, redirect, render_template, request
from flask.typing import ResponseReturnValue

from freeplay_server.accounts.users import Roles
from freeplay_server.auth.auth_filter import allow_role
from freeplay_server.projects.project_creator import ProjectCreator, ProjectCreationFailure
from freeplay_server.projects.project_page_blueprint_filters import ProjectPageBlueprintFilters
from freeplay_server.projects.projects_repository import ProjectRecord, ProjectsRepository


def project_list_page(
        project_filters: ProjectPageBlueprintFilters,
        project_creator: ProjectCreator,
        projects_repo: ProjectsRepository) -> Blueprint:
    page = Blueprint('project_list_page', __name__, url_prefix='/projects')

    @page.url_value_preprocessor
    def hydrate_projects(_: Optional[str], values: Optional[dict[str, Any]]) -> None:
        project_filters.hydrate_projects(values)

    @allow_role(Roles.ACCOUNT_USER)
    @page.get("")
    def show() -> ResponseReturnValue:
        all_projects: list[ProjectRecord] = projects_repo.find_all()
        return render_template(
            'project_list.html',
            all_projects=all_projects,
            new_link="/projects/new-project"
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/new-project')
    def new_project() -> ResponseReturnValue:
        return render_template(
            'new_project.html',
            cancel_link='/projects',
            name=''
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/new-project')
    def create_project() -> ResponseReturnValue:
        name = request.form['name']
        result = project_creator.try_create(name=name)

        if type(result) is ProjectCreationFailure:
            return render_template(
                'new_project.html',
                cancel_link=f'/projects',
                name=name,
                error_message=result.value
            ), 400
        success = cast(ProjectRecord, result)
        return redirect(f"/projects/{success.id}")

    @allow_role(Roles.ACCOUNT_USER)
    @page.delete("/<uuid:selected_project_id>")
    def delete_project(selected_project_id: UUID) -> ResponseReturnValue:
        # Warning -- the project_id parameter name is stripped by hydrate_projects
        projects_repo.delete(selected_project_id)

        all_projects: list[ProjectRecord] = projects_repo.find_all()
        return render_template(
            'project_list.html',
            all_projects=all_projects,
            new_link="/projects/new-project"
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.get("/request_deletion/<uuid:selected_project_id>")
    def request_deletion(selected_project_id: UUID) -> ResponseReturnValue:
        # Warning -- the project_id parameter name is stripped by hydrate_projects
        return render_template(
            'deletion_confirmation_modal.html',
            project_id=selected_project_id,
        )

    return page
