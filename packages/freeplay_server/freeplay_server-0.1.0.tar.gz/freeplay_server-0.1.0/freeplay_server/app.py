import logging
import os
from datetime import timedelta
from typing import Optional

from flask import Flask, redirect, render_template, request
from flask.sessions import SessionInterface
from flask.typing import ResponseReturnValue
from flask_session import Session
from flask_swagger_ui import get_swaggerui_blueprint  # type: ignore
from werkzeug.exceptions import HTTPException

from freeplay_server.accounts.account_show_page import account_show_page
from freeplay_server.accounts.accounts_blueprint_filters import AccountsBlueprintFilters
from freeplay_server.accounts.accounts_repository import AccountsRepository
from freeplay_server.accounts.default_administration import DefaultAdministration
from freeplay_server.accounts.user_creator import UserCreator
from freeplay_server.app_environment import AppEnvironment
from freeplay_server.auth.api_key_service import ApiKeyService
from freeplay_server.auth.api_keys_repository import ApiKeysRepository
from freeplay_server.auth.auth_filter import AuthFilter, public_endpoint
from freeplay_server.comparisons.comparisons_page import comparisons_page
from freeplay_server.comparisons.comparisons_service import ComparisonsService
from freeplay_server.database_support.database_gateway import DatabaseGateway
from freeplay_server.evaluations.auto_eval_processor import AutoEvalProcessor
from freeplay_server.extensions import sa
from freeplay_server.health_api import health_api
from freeplay_server.login.login_page import login_page
from freeplay_server.project_sessions.project_sessions_api import project_sessions_api
from freeplay_server.project_sessions.project_sessions_page import project_sessions_page
from freeplay_server.project_sessions.project_sessions_repository import ProjectSessionsRepository
from freeplay_server.project_sessions.session_display_service import SessionDisplayService
from freeplay_server.projects.project_creator import ProjectCreator
from freeplay_server.projects.project_list_page import project_list_page
from freeplay_server.projects.project_page_blueprint_filters import ProjectPageBlueprintFilters
from freeplay_server.projects.projects_repository import ProjectsRepository
from freeplay_server.prompt_templates.llm_model_repository import LLMModelRepository
from freeplay_server.prompt_templates.prompt_template_version_repository import PromptTemplateVersionRepository
from freeplay_server.prompt_templates.prompt_templates_api import prompt_templates_api
from freeplay_server.prompt_templates.prompt_templates_list_page import prompt_templates_list_page
from freeplay_server.prompt_templates.prompt_templates_page import prompt_templates_page
from freeplay_server.record.record_api import record_api
from freeplay_server.record.session_recorder import SessionRecorder
from freeplay_server.service_dependencies import ServiceDependencies
from freeplay_server.settings.settings_api_access import api_access_show_page
from freeplay_server.settings.settings_environment_creator import EnvironmentCreator
from freeplay_server.settings.settings_environments import environments_show_page
from freeplay_server.settings.settings_models import models_show_page
from freeplay_server.settings.settings_repository import EnvironmentsRepository
from freeplay_server.settings.settings_repository import ModelsRepository
from freeplay_server.test_lists.test_lists_page import test_lists_page
from freeplay_server.test_lists.test_lists_repository import TestListsRepository
from freeplay_server.test_runs.test_runs_api import build_test_runs_api
from freeplay_server.test_runs.test_runs_page import test_runs_page
from freeplay_server.test_runs.test_runs_service import TestRunsService

DATABASE_OPTIONS = {"pool_pre_ping": True, "pool_recycle": 300, "pool_size": 16}


# Note: This method must be called before any log statements -- this configures log level and
# scoping for all future logger instantiations in the application.
def configure_logger() -> None:
    logging.basicConfig(level=os.environ.get('ROOT_LOG_LEVEL', 'INFO'))
    logging.getLogger('freeplay_server').setLevel(level=os.environ.get('FREEPLAY_LOG_LEVEL', 'INFO'))


def create_app() -> Flask:
    return create_app_from_env(AppEnvironment.from_env())


def create_app_from_env(
        env: AppEnvironment,
        service_dependencies: Optional[ServiceDependencies] = None,
        session_interface_override: Optional[SessionInterface] = None
) -> Flask:
    # This method must be called above any logger references
    configure_logger()
    logger = logging.getLogger(__name__)

    if not service_dependencies:
        service_dependencies = ServiceDependencies.from_app_environment(env)

    app = Flask(__name__)

    # Database setup
    app.config["SQLALCHEMY_DATABASE_URI"] = env.database_url
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = DATABASE_OPTIONS
    app.config["SQLALCHEMY_ECHO"] = False
    sa.init_app(app)

    # Auto Evaluation setup
    with app.app_context():
        db = DatabaseGateway(sa.engine)
        auto_eval_processor = AutoEvalProcessor(
            sa.engine,
            service_dependencies.freeplay_client,
            env.auto_eval_freeplay_config,
            service_dependencies.datadog_client)

    accounts_repo = AccountsRepository(db=db)

    api_key_repo = ApiKeysRepository(db)
    api_key_service = ApiKeyService(api_key_repo)
    auth_filter = AuthFilter(accounts_repo, app, env.api_key, api_key_service)

    user_creator = UserCreator(repo=accounts_repo, stytch_client=service_dependencies.stytch_client)
    accounts_blueprint_filters = AccountsBlueprintFilters(accounts_repo)
    default_administration = DefaultAdministration(
        accounts_repo=accounts_repo,
        api_key_service=api_key_service,
        stytch_client=service_dependencies.stytch_client)

    projects_repo = ProjectsRepository(db=db)
    llm_model_repo = LLMModelRepository(db=db)
    project_creator = ProjectCreator(db=db)
    environments_repo = EnvironmentsRepository(db=db)
    models_repo = ModelsRepository(db=db)
    prompt_template_version_repo = PromptTemplateVersionRepository(
        db=db,
        llm_model_repository=llm_model_repo,
        environments_repository=environments_repo
    )
    project_sessions_repo = ProjectSessionsRepository(
        db=db,
        llm_models_repo=llm_model_repo,
        api_key_repo=api_key_repo
    )

    test_lists_repo = TestListsRepository(db=db)
    comparisons_service = ComparisonsService(db=db,
                                             test_lists_repo=test_lists_repo,
                                             project_sessions_repo=project_sessions_repo,
                                             prompt_template_version_repo=prompt_template_version_repo)

    test_runs_service = TestRunsService(
        db=db, project_sessions_repo=project_sessions_repo, test_lists_repo=test_lists_repo)

    session_recorder = SessionRecorder(db=db, project_sessions_repository=project_sessions_repo)
    session_display_service = SessionDisplayService(project_sessions_repo, test_lists_repo)

    project_page_blueprint_filters = ProjectPageBlueprintFilters(
        lambda project_id: projects_repo.try_find(project_id),
        projects_repo.find_all,
    )

    environment_creator = EnvironmentCreator(db=db)

    if env.default_admin_user_email_addresses:
        admin_users = env.default_admin_user_email_addresses.split('|')

        for user in admin_users:
            logger.info(f'Creating default admin user {user}')
            default_administration.provision(user, is_internal_user=True, is_admin_user=True)

    if env.default_account_user_email_addresses:
        normal_users = env.default_account_user_email_addresses.split('|')

        for user in normal_users:
            logger.info(f'Creating default account user {user}')
            default_administration.provision(user, is_internal_user=True)

    # Flask-Session setup
    if session_interface_override:
        app.session_interface = session_interface_override
    else:
        app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(weeks=1)
        app.config["SESSION_TYPE"] = 'sqlalchemy'
        app.config["SESSION_SQLALCHEMY"] = sa
        Session(app)

    @app.before_request
    def remove_trailing_slash() -> ResponseReturnValue | None:
        rp = request.path
        if rp != '/' and rp.endswith('/'):
            return redirect(rp[:-1], code=301)

        return None

    @public_endpoint
    @app.get('/')
    def root_redirect() -> ResponseReturnValue:
        return redirect('/projects')

    @app.errorhandler(404)
    def page_not_found(_e: HTTPException) -> ResponseReturnValue:
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(_e: HTTPException) -> ResponseReturnValue:
        return render_template('500.html'), 500

    # Register app-wide filters _before_ any blueprints are registered
    app.before_request(auth_filter.enforce_auth)
    app.before_request(auth_filter.check_tos_acceptance)

    # Register (UI) Pages
    app.register_blueprint(login_page(
        stytch_client=service_dependencies.stytch_client,
        base_url=env.api_url,
        stytch_public_token=env.stytch_public_token,
        accounts_repo=accounts_repo
    ))

    app.register_blueprint(api_access_show_page(
        filters=accounts_blueprint_filters,
        project_filters=project_page_blueprint_filters,
        api_key_service=api_key_service,
        api_key_repo=api_key_repo,
    ))

    app.register_blueprint(account_show_page(
        filters=accounts_blueprint_filters,
        project_filters=project_page_blueprint_filters,
        user_creator=user_creator,
        accounts_repo=accounts_repo,
    ))

    app.register_blueprint(environments_show_page(
        environments_repo=environments_repo,
        environment_creator=environment_creator,
        project_filters=project_page_blueprint_filters,
    ))

    app.register_blueprint(models_show_page(
        filters=project_page_blueprint_filters,
        models_repo=models_repo,
    ))

    app.register_blueprint(project_list_page(
        project_filters=project_page_blueprint_filters,
        project_creator=project_creator,
        projects_repo=projects_repo
    ))
    app.register_blueprint(prompt_templates_list_page(
        filters=project_page_blueprint_filters,
        prompt_template_version_repo=prompt_template_version_repo,
        llm_model_repository=llm_model_repo,
        environments_repo=environments_repo,
    ))
    app.register_blueprint(prompt_templates_page(
        filters=project_page_blueprint_filters,
        prompt_template_version_repo=prompt_template_version_repo,
        llm_model_repository=llm_model_repo,
        environments_repo=environments_repo,
        api_url=env.api_url,
    ))
    app.register_blueprint(project_sessions_page(
        filters=project_page_blueprint_filters,
        sessions_repo=project_sessions_repo,
        test_list_repo=test_lists_repo,
        prompt_template_version_repo=prompt_template_version_repo,
        llm_model_repo=llm_model_repo,
        session_display_service=session_display_service,
    ))
    app.register_blueprint(
        test_lists_page(
            filters=project_page_blueprint_filters,
            repo=test_lists_repo,
            test_runs_service=test_runs_service,
            project_sessions_repo=project_sessions_repo,
            prompt_template_version_repo=prompt_template_version_repo,
            api_url=env.api_url))

    app.register_blueprint(test_runs_page(
        filters=project_page_blueprint_filters,
        test_runs_service=test_runs_service,
        project_sessions_repo=project_sessions_repo,
        session_display_service=session_display_service))

    app.register_blueprint(
        comparisons_page(
            filters=project_page_blueprint_filters,
            comparisons_service=comparisons_service,
            test_runs_service=test_runs_service
        ))

    # Register APIs
    app.register_blueprint(
        project_sessions_api(
            projects_repo=projects_repo))

    app.register_blueprint(
        build_test_runs_api(
            filters=project_page_blueprint_filters,
            test_list_repo=test_lists_repo,
            test_runs=test_runs_service))

    app.register_blueprint(
        prompt_templates_api(filters=project_page_blueprint_filters,
                             prompt_template_version_repo=prompt_template_version_repo))

    app.register_blueprint(
        record_api(
            recorder=session_recorder,
            auto_eval_processor=auto_eval_processor))

    app.register_blueprint(
        health_api(
            db=db))

    app.register_blueprint(get_swaggerui_blueprint(
        "/docs",
        "/static/docs/freeplay_api_spec.yaml",
    ))

    return app
