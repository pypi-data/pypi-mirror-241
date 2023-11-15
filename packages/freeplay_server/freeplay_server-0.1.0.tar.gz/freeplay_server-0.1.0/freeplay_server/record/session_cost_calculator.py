import logging
from dataclasses import dataclass
from decimal import *
from typing import Optional

from freeplay_server.record.token_counting import TokenCounts

logger = logging.getLogger(__name__)

@dataclass
class SessionCost:
    prompt_token_cost: Decimal
    return_token_cost: Decimal


@dataclass
class ProviderPriceConfig:
    prompt_cost: Decimal
    response_cost: Decimal


model_cost_per_token: dict[str, ProviderPriceConfig] = {
    "gpt-3.5-turbo-0613": ProviderPriceConfig(
        prompt_cost=Decimal('0.0000015'),
        response_cost=Decimal('0.000002')
    ),
    "gpt-3.5-turbo-16k-0613": ProviderPriceConfig(
        prompt_cost=Decimal('0.000003'),
        response_cost=Decimal('0.000004')
    ),
    "gpt-3.5-turbo-16k": ProviderPriceConfig(
        prompt_cost=Decimal('0.000003'),
        response_cost=Decimal('0.000004')
    ),
    "gpt-3.5-turbo": ProviderPriceConfig(
        prompt_cost=Decimal('0.0000015'),
        response_cost=Decimal('0.000002')
    ),
    "gpt-3.5-turbo-1106": ProviderPriceConfig(
        prompt_cost=Decimal('0.000001'),
        response_cost=Decimal('0.000002')
    ),
    "gpt-3.5-turbo-instruct": ProviderPriceConfig(
        prompt_cost=Decimal('0.0000015'),
        response_cost=Decimal('0.000002')
    ),
    "gpt-4-0314": ProviderPriceConfig(
        prompt_cost=Decimal('0.00003'),
        response_cost=Decimal('0.00006')
    ),
    "gpt-4-32k-0314": ProviderPriceConfig(
        prompt_cost=Decimal('0.00006'),
        response_cost=Decimal('0.00012')
    ),
    "gpt-4-0613": ProviderPriceConfig(
        prompt_cost=Decimal('0.00003'),
        response_cost=Decimal('0.00006')
    ),
    "gpt-4-32k-0613": ProviderPriceConfig(
        prompt_cost=Decimal('0.00006'),
        response_cost=Decimal('0.00012')
    ),
    "gpt-4-1106-preview": ProviderPriceConfig(
        prompt_cost=Decimal('0.00001'),
        response_cost=Decimal('0.00003')
    ),
    "gpt-4": ProviderPriceConfig(
        prompt_cost=Decimal('0.00003'),
        response_cost=Decimal('0.00006')
    ),
    "text-davinci-003": ProviderPriceConfig(
        prompt_cost=Decimal('0.00002'),
        response_cost=Decimal('0.00002'),
    ),
    "claude-v1": ProviderPriceConfig(
        prompt_cost=Decimal('0.00000163'),
        response_cost=Decimal('0.00000551')
    ),
    "claude-1": ProviderPriceConfig(
        prompt_cost=Decimal('0.00000163'),
        response_cost=Decimal('0.00000551')
    ),
    "claude-2": ProviderPriceConfig(
        prompt_cost=Decimal('0.00001102'),
        response_cost=Decimal('0.00003268')
    ),
    "claude-instant-1": ProviderPriceConfig(
        prompt_cost=Decimal('0.00000163'),
        response_cost=Decimal('0.00000551')
    ),
    "azure-gpt-3.5-turbo": ProviderPriceConfig(
        prompt_cost=Decimal('0.0000015'),
        response_cost=Decimal('0.000002')
    ),
    "azure-gpt-3.5-turbo-16k": ProviderPriceConfig(
        prompt_cost=Decimal('0.000003'),
        response_cost=Decimal('0.000004')
    ),
    "azure-gpt-4": ProviderPriceConfig(
        prompt_cost=Decimal('0.00003'),
        response_cost=Decimal('0.00006')
    ),
    "azure-gpt-4-32k": ProviderPriceConfig(
        prompt_cost=Decimal('0.00006'),
        response_cost=Decimal('0.00012')
    ),
}


class SessionCostCalculator:
    @staticmethod
    def calculate_cost(model: str, token_counts: TokenCounts) -> Optional[SessionCost]:
        if model in model_cost_per_token:
            costs = model_cost_per_token[model]
            prompt_cost = token_counts.prompt_token_count * costs.prompt_cost
            response_cost = token_counts.return_token_count * costs.response_cost

            return SessionCost(
                prompt_token_cost=prompt_cost,
                return_token_cost=response_cost
            )
        else:
            logger.warning(f"Warning: model not found: {model}")
            return None
