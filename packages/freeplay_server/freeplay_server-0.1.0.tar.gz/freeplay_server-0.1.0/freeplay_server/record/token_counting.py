import json
import logging
from dataclasses import dataclass
from typing import Optional, cast

import anthropic  # type: ignore
import tiktoken

logger = logging.getLogger(__name__)


# Note that the logic for this class was pulled from OpenAI's Cookbook Example here:
# https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb

@dataclass
class TokenCounts:
    prompt_token_count: int
    return_token_count: int


class TokenCounting:
    OPENAI_CHAT_MODELS = {
        "azure-gpt-3.5-turbo",
        "azure-gpt-3.5-turbo-16k",
        "azure-gpt-4",
        "azure-gpt-4-32k",
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-1106",
        "gpt-3.5-turbo-16k-0613",
        "gpt-3.5-turbo-16k",
        "gpt-3.5-turbo",
        "gpt-4-0314",
        "gpt-4-32k-0314",
        "gpt-4-0613",
        "gpt-4-1106-preview",
        "gpt-4-32k-0613",
        "gpt-4"
    }

    OPENAI_TEXT_MODELS = {
        "text-davinci-003",
        "gpt-3.5-turbo-instruct",
    }

    ANTHROPIC_MODELS = {
        "claude-v1",
        "claude-1",
        "claude-2",
        "claude-instant-1"
    }

    @staticmethod
    def num_tokens_from_messages(messages_string: str, model: str = "gpt-3.5-turbo-0613") -> Optional[int]:
        parsed_json = json.loads(messages_string)
        try:
            encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            logger.warning("Warning: model not found. Using cl100k_base encoding.")
            encoding = tiktoken.get_encoding("cl100k_base")
        if model in {
            "gpt-3.5-turbo-0613",
            "gpt-3.5-turbo-16k-0613",
            "gpt-3.5-turbo-16k",
            "gpt-3.5-turbo-1106",
            "gpt-4-0314",
            "gpt-4-32k-0314",
            "gpt-4-0613",
            "gpt-4-32k-0613",
        }:
            tokens_per_message = 3
            tokens_per_name = 1
        elif model == "gpt-3.5-turbo-0301":
            tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
            tokens_per_name = -1  # if there's a name, the role is omitted
        elif "gpt-3.5-turbo" in model:
            logger.info("Received model: gpt-3.5-turbo. Returning num tokens assuming gpt-3.5-turbo-0613.")
            return TokenCounting.num_tokens_from_messages(messages_string, model="gpt-3.5-turbo-0613")
        elif "gpt-4" in model:
            logger.info("Received model: gpt-4. Returning num tokens assuming gpt-4-0613.")
            return TokenCounting.num_tokens_from_messages(messages_string, model="gpt-4-0613")
        else:
            logger.info(f"Received model: {model}. Unable to count tokens for this model type. Returning None.")
            return None
        num_tokens = 0
        for message in parsed_json:
            num_tokens += tokens_per_message
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":
                    num_tokens += tokens_per_name
        num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
        return num_tokens

    @staticmethod
    def num_tokens_from_string(prompt: str, encoding_name: str = "cl100k_base") -> int:
        encoding = tiktoken.get_encoding(encoding_name)
        num_tokens = len(encoding.encode(prompt))
        return num_tokens

    @staticmethod
    def num_tokens_from_string_anthropic(prompt: str) -> int:
        num_tokens = anthropic.count_tokens(prompt)
        return cast(int, num_tokens)

    def count_tokens(self, model: str, prompt_content: str, return_content: str) -> Optional[TokenCounts]:
        if model in self.OPENAI_CHAT_MODELS:
            chat_token_counts = TokenCounting.num_tokens_from_messages(prompt_content, model=model)
            return TokenCounts(
                chat_token_counts,
                TokenCounting.num_tokens_from_string(return_content)
            ) if chat_token_counts else None
        elif model in self.OPENAI_TEXT_MODELS:
            return TokenCounts(
                TokenCounting.num_tokens_from_string(prompt_content),
                TokenCounting.num_tokens_from_string(return_content)
            )
        elif model in self.ANTHROPIC_MODELS:
            return TokenCounts(
                TokenCounting.num_tokens_from_string_anthropic(prompt_content),
                TokenCounting.num_tokens_from_string_anthropic(return_content)
            )
        else:
            # Handle no model set or model not in supported token counter.
            return None
