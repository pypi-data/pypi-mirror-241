from typing import Optional, Any
from uuid import UUID

from flask import (
    Blueprint,
    jsonify,
    redirect,
    render_template,
    request,
)
from flask.typing import ResponseReturnValue

from freeplay_server.accounts.users import Roles
from freeplay_server.auth.auth_filter import allow_role
from freeplay_server.projects.project_page_blueprint_filters import ProjectPageBlueprintFilters
from freeplay_server.settings.settings_environment_creator import (
    EnvironmentCreator,
    EnvironmentCreationFailure,
)
from freeplay_server.settings.settings_repository import EnvironmentsRepository
from freeplay_server.web_support.api_support import try_parse_uuid


def environments_show_page(
        environments_repo: EnvironmentsRepository,
        environment_creator: EnvironmentCreator,
        project_filters: ProjectPageBlueprintFilters,
) -> Blueprint:
    page = Blueprint('environments_show_page', __name__, url_prefix='/settings/environments')

    @page.url_value_preprocessor
    def hydrate_projects(_: Optional[str], values: Optional[dict[str, Any]]) -> None:
        project_filters.hydrate_projects(values)

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('')
    def show_environments() -> ResponseReturnValue:
        all_environments = environments_repo.find_all()
        return render_template(
            'environments_list.html',
            all_environments=all_environments,
            new_link="/settings/environments/new-environment"
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/new-environment')
    def request_new_environment() -> ResponseReturnValue:
        return render_template(
            'new_environment.html',
            cancel_link='/settings/environments',
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/new-environment')
    def create_new_environment() -> ResponseReturnValue:
        name = request.form['name']
        result = environment_creator.try_create(name=name)
        if type(result) is EnvironmentCreationFailure:
            return render_template(
                'new_environment.html',
                cancel_link='/settings/environments',
                name=name,
                error_message=result.value
            ), 400

        return redirect("/settings/environments")

    @allow_role(Roles.ACCOUNT_USER)
    @page.get('/<environment_id_arg>')
    def edit_view_environment(environment_id_arg: str) -> ResponseReturnValue:
        environment_id = try_parse_uuid(environment_id_arg)
        if environment_id is None:
            return jsonify({'error': 'Not Found'}), 404

        environment_details = environments_repo.try_find(environment_id=environment_id)
        if environment_details:
            return render_template(
                'edit_environment.html',
                cancel_link='/settings/environments',
                is_creating=False,
                name=environment_details.name,
                environment_id=environment_details.id
            )

        return redirect('/settings/environments')

    @allow_role(Roles.ACCOUNT_USER)
    @page.post("/request_edition/<environment_id_arg>")
    def request_edit_environment(environment_id_arg: str) -> ResponseReturnValue:
        environment_id = try_parse_uuid(environment_id_arg)
        if environment_id is None:
            return jsonify({'error': 'Not Found'}), 404

        environment_details = environments_repo.try_find(environment_id=environment_id)
        if environment_details is None:
            return jsonify({'error': 'Not Found'}), 404

        name = request.form['name']
        environments_repo.update_environment_name(
            environment_id=environment_id,
            name=name
        )
        return redirect("/settings/environments")

    @allow_role(Roles.ACCOUNT_USER)
    @page.post('/<environment_id_arg>')
    def edit_environment(environment_id_arg: str) -> ResponseReturnValue:
        environment_id = try_parse_uuid(environment_id_arg)
        if environment_id is None:
            return jsonify({'error': 'Not Found'}), 404

        environment_details = environments_repo.try_find(environment_id=environment_id)
        if environment_details is None:
            return jsonify({'error': 'Not Found'}), 404

        name = request.form['name']
        environments_repo.update_environment_name(
            environment_id=environment_id,
            name=name
        )
        return redirect("/settings/environments")

    @allow_role(Roles.ACCOUNT_USER)
    @page.get("/request_deletion/<environment_id_arg>")
    def request_deletion(environment_id_arg: UUID) -> ResponseReturnValue:
        return render_template(
            'environment_deletion_confirmation_modal.html',
            environment_id=environment_id_arg,
            is_deleting=True,
        )

    @allow_role(Roles.ACCOUNT_USER)
    @page.delete('/<environment_id_arg>')
    def delete_environment(environment_id_arg: str) -> ResponseReturnValue:
        environment_id = try_parse_uuid(environment_id_arg)
        if environment_id is None:
            return jsonify({'error': 'Not Found'}), 404

        environment_details = environments_repo.try_find(environment_id=environment_id)
        if environment_details is None:
            return jsonify({'error': 'Not Found'}), 404

        environments_repo.soft_delete_environment(environment_details.id)
        return jsonify({})

    return page
