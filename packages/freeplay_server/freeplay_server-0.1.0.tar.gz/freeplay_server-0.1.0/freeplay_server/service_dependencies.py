from freeplay import Freeplay
from freeplay.provider_config import ProviderConfig, OpenAIConfig
from stytch import Client

from freeplay_server.app_environment import AppEnvironment
from freeplay_server.monitoring.datadog_client import DatadogClient


class ServiceDependencies:

    @staticmethod
    def from_app_environment(app_environment: AppEnvironment) -> 'ServiceDependencies':
        stytch_client = Client(
            app_environment.stytch_project,
            app_environment.stytch_secret,
            app_environment.stytch_environment
        )
        freeplay_client = Freeplay(
            app_environment.auto_eval_freeplay_config.api_key,
            app_environment.auto_eval_freeplay_config.api_base,
            provider_config=ProviderConfig(openai=OpenAIConfig(
                app_environment.auto_eval_freeplay_config.openai_api_key
            ))
        )
        # Initialize for datadog logging. Triggers side-effects.
        datadog_client = DatadogClient()

        return ServiceDependencies(
            stytch_client=stytch_client,
            freeplay_client=freeplay_client,
            datadog_client=datadog_client
        )

    def __init__(
            self,
            stytch_client: Client,
            freeplay_client: Freeplay,
            datadog_client: DatadogClient
    ):
        self.stytch_client = stytch_client
        self.freeplay_client = freeplay_client
        self.datadog_client = datadog_client
