import re
from dataclasses import dataclass
from typing import Optional

from freeplay_server.web_support import json_support


@dataclass
class ChatMessage:
    role: str
    content: str


PROMPT_VARIABLE_REGEX = re.compile(r"{{(\w+)}}")


# Domain object that encapsulates a prompt (interpolated or not) which may have raw text or a
# set of messages, depending on the template type
@dataclass
class PromptModel:
    messages: list[ChatMessage]

    @classmethod
    def from_string(cls, interpolated_prompt: Optional[str]) -> 'PromptModel':
        if interpolated_prompt is None or interpolated_prompt == "":
            raise ValueError('Unable to format prompt without content.')

        messages = json_support.force_decode_list(ChatMessage, interpolated_prompt.encode('utf-8'))
        return PromptModel(messages)

    def format(self, variables: dict[str, str]) -> 'PromptModel':
        messages = [ChatMessage(
            role=message.role,
            content=PROMPT_VARIABLE_REGEX.sub(lambda match: variables.get(match.group(1), ''), message.content)
        ) for message in self.messages] if self.messages else []

        return PromptModel(
            messages
        )
