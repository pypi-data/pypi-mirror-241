import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class AutoEvalFreeplayConfig:
    api_base: str
    api_key: str
    openai_api_key: str
    project_id: str
    template_environment: str
    template_name: str


@dataclass
class AppEnvironment:
    port: int
    # This is actually just the root URL, and you must add /api to make it the API URL.
    api_url: str
    function_url: str
    database_url: str
    use_local_code_executor: bool
    use_flask_debug_mode: bool
    default_admin_user_email_addresses: Optional[str]
    default_account_user_email_addresses: Optional[str]

    @classmethod
    def __require_env(cls, name: str) -> str:
        value = os.environ.get(name)
        if value is None:
            raise Exception(f"Failed to read {name} from the environment")
        return value

    def __init__(self,
                 port: int,
                 api_url: str,
                 api_key: str,
                 function_url: str,
                 database_url: str,
                 stytch_project: str,
                 stytch_secret: str,
                 stytch_public_token: str,
                 stytch_environment: str,
                 default_admin_user_email_addresses: Optional[str],
                 default_account_user_email_addresses: Optional[str],
                 use_local_code_executor: bool,
                 use_flask_debug_mode: bool,
                 auto_eval_freeplay_config: AutoEvalFreeplayConfig) -> None:
        self.port = port
        self.api_url = api_url
        self.api_key = api_key
        self.function_url = function_url
        self.database_url = database_url
        self.stytch_secret = stytch_secret
        self.stytch_project = stytch_project
        self.stytch_public_token = stytch_public_token
        self.stytch_environment = stytch_environment
        self.default_admin_user_email_addresses = default_admin_user_email_addresses
        self.default_account_user_email_addresses = default_account_user_email_addresses
        self.use_local_code_executor = use_local_code_executor
        self.use_flask_debug_mode = use_flask_debug_mode
        self.auto_eval_freeplay_config = auto_eval_freeplay_config

    @classmethod
    def from_env(cls) -> 'AppEnvironment':
        return cls(
            port=int(os.environ.get('PORT', 8080)),
            api_url=cls.__require_env('FREEPLAY_API_URL'),
            api_key=cls.__require_env('FREEPLAY_API_KEY'),
            function_url=cls.__require_env('FREEPLAY_EXECUTE_FUNCTION_URL'),
            database_url=cls.__require_env('FREEPLAY_DB_URL'),
            stytch_project=cls.__require_env('STYTCH_PROJECT_ID'),
            stytch_secret=cls.__require_env('STYTCH_SECRET'),
            stytch_public_token=cls.__require_env('STYTCH_PUBLIC_TOKEN'),
            stytch_environment=cls.__require_env('STYTCH_ENVIRONMENT'),
            default_account_user_email_addresses=os.environ.get('DEFAULT_ACCOUNT_USER_EMAIL_ADDRESSES'),
            default_admin_user_email_addresses=os.environ.get('DEFAULT_ADMIN_USER_EMAIL_ADDRESSES'),
            use_local_code_executor=os.environ.get('FREEPLAY_USE_LOCAL_CODE_EXECUTOR', 'false') == 'true',
            use_flask_debug_mode=os.environ.get('FREEPLAY_USE_FLASK_DEBUG_MODE', 'false') == 'true',
            auto_eval_freeplay_config=AutoEvalFreeplayConfig(
                api_base="https://prod.freeplay.ai/api",
                openai_api_key=cls.__require_env('DOGFOOD_OPENAI_API_KEY'),
                api_key=cls.__require_env('DOGFOOD_FREEPLAY_API_KEY'),
                project_id='28a2541d-fe3a-4919-8166-538698ee9a71',
                template_environment=os.getenv('DOGFOOD_FREEPLAY_ENVIRONMENT', 'prod'),
                template_name='auto-evals'
            )
        )
