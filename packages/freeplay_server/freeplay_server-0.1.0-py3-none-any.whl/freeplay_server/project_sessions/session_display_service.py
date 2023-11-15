from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass
from enum import StrEnum
from typing import Optional, Tuple
from uuid import UUID

from flask import g

from freeplay_server.evaluations.eval_page import EvaluationCriteriaInfo, EvaluationResultInfo
from freeplay_server.evaluations.evaluations_repository import evaluations_for_session
from freeplay_server.extensions import sa
from freeplay_server.models import EvaluationCriteria, EvaluationResult
from freeplay_server.project_sessions.project_sessions import ProjectSessionCalculator
from freeplay_server.project_sessions.project_sessions_repository import ProjectSessionEntryDetailsRecord, \
    ProjectSessionsRepository, ProjectSessionDetailsRecord, FunctionCall
from freeplay_server.project_sessions.prompt_model import ChatMessage, PromptModel
from freeplay_server.test_lists.test_lists_page import TestListInfo
from freeplay_server.test_lists.test_lists_repository import TestListsRepository, TestListRecord
from freeplay_server.utilities.formatters import format_decimal_dollars, format_latency


class SessionEntryGroupType(StrEnum):
    Chain = 'chain'
    Chat = 'chat'


@dataclass
class DisplayMetadataInfo:
    field: str
    value: str
    link: Optional[str] = None
    is_env_deleted: Optional[bool] = False


Evaluations = list[tuple[EvaluationCriteria, Optional[EvaluationResult]]]


@dataclass
class DisplayableSessionGroup:
    prompt_name: str
    prompt_metadata: list[DisplayMetadataInfo]
    prompt_template_content: PromptModel
    cost: Optional[str]
    content: Optional[PromptModel]
    response: str
    session_latency: Optional[str]
    evaluations: list[tuple[EvaluationCriteriaInfo, Optional[EvaluationResultInfo]]]
    function_call_response: Optional[FunctionCall]
    function_specification: Optional[str]


@dataclass
class SessionEntryGroup:
    type: SessionEntryGroupType
    display_info: DisplayableSessionGroup

    @staticmethod
    def session_entry_group_metadata_pairs(
            session_entry: ProjectSessionEntryDetailsRecord,
            project_id: UUID
    ) -> Tuple[list[DisplayMetadataInfo], Optional[str]]:
        metadata = []
        if session_entry.llm_provider and session_entry.llm_model:
            metadata.append(
                DisplayMetadataInfo("Provider", f"{session_entry.llm_provider} ({session_entry.llm_model})"))

        function_spec = None
        for param, value in session_entry.llm_parameters.items():
            if param == 'functions':
                function_spec = value
            metadata.append(DisplayMetadataInfo(param, value))

        if session_entry.api_key_name:
            metadata.append(DisplayMetadataInfo(
                "API Key", session_entry.api_key_name))

        return_token_count = session_entry.return_token_count
        prompt_token_count = session_entry.prompt_token_count
        if return_token_count and prompt_token_count:
            metadata.append(DisplayMetadataInfo("Tokens", f'{return_token_count + prompt_token_count:,}'))

        template_version_url = \
            f'/projects/{project_id}/templates/{session_entry.prompt_template_id}/versions/{session_entry.prompt_template_version_id}'
        metadata.append(DisplayMetadataInfo("Version", session_entry.template_name, template_version_url))

        if session_entry.environment_name:
            metadata.append(DisplayMetadataInfo(
                "Environment", session_entry.environment_name, is_env_deleted=session_entry.is_env_deleted))

        return metadata, function_spec

    @classmethod
    def from_entry(
            cls,
            entry: ProjectSessionEntryDetailsRecord,
            type: SessionEntryGroupType,
            evaluations: Evaluations,
            project_id: UUID,
            override_content: Optional[PromptModel] = None,
    ) -> 'SessionEntryGroup':
        formatted_inputs = dict()

        for variable_key, variable_value in entry.inputs.items():
            formatted_inputs[variable_key] = f'{{{{{variable_key}: {variable_value}}}}}'

        metadatas, function_specification = SessionEntryGroup.session_entry_group_metadata_pairs(entry, project_id)
        maybe_cost = ProjectSessionCalculator.calculate_costs(entry.prompt_token_cost, entry.return_token_cost)
        return SessionEntryGroup(
            type,
            DisplayableSessionGroup(
                entry.template_name,
                metadatas,
                entry.template_content.format(formatted_inputs),
                format_decimal_dollars(maybe_cost) if maybe_cost else None,
                override_content or entry.interpolated_prompt_content,
                entry.response,
                session_latency=format_latency(entry.session_latency) if entry.session_latency else None,
                evaluations=[(EvaluationCriteriaInfo(ec), EvaluationResultInfo(er) if er else None) for (ec, er) in
                             evaluations],
                function_call_response=entry.function_call_response,
                function_specification=function_specification,
            ))


@dataclass
class TestListInfoWithSelection:
    info: TestListInfo
    selected: bool


@dataclass
class SessionDisplayInfo:
    created_at: int
    session_id: UUID
    session_groups: list[SessionEntryGroup]
    session_overview: list[DisplayMetadataInfo]
    evaluations: list[tuple[EvaluationCriteriaInfo, Optional[EvaluationResultInfo]]]
    test_lists: list[TestListInfoWithSelection]


class SessionDisplayService:

    def __init__(self, sessions_repo: ProjectSessionsRepository, test_list_repo: TestListsRepository):
        self.sessions_repo = sessions_repo
        self.test_list_repo = test_list_repo

    # This method groups sessions into "Groups", which are a concept useful in understanding a session.
    # A session group is either:
    # 1. A chain (single prompt or many prompts run in succession)
    # 2. A continuous chat session (a series of recorded entries that add to a history).
    # One session may encapsulate many session groups.
    def __fold_session_into_groups(
            self,
            session_details: ProjectSessionDetailsRecord,
            all_evaluations: Evaluations,
            project_id: UUID
    ) -> list[SessionEntryGroup]:
        session_groups = []
        is_continued_conversation = False

        evaluations_by_prompt: dict[UUID, Evaluations] = defaultdict(list)
        for criteria, result in all_evaluations:
            evaluations_by_prompt[criteria.prompt_template_id].append((criteria, result))

        for index, entry in enumerate(session_details.entries):
            try:
                next_entry = session_details.entries[index + 1]
            except IndexError:
                next_entry = None
            evaluations = evaluations_by_prompt[entry.prompt_template_id]

            if next_entry and next_entry.template_name == entry.template_name:
                # Handle chat prompts, which may be continuous chat or single completions
                if entry.interpolated_prompt_content and entry.interpolated_prompt_content.messages and next_entry.interpolated_prompt_content and next_entry.interpolated_prompt_content.messages:
                    zipped_messages = zip(
                        next_entry.interpolated_prompt_content.messages if next_entry.interpolated_prompt_content else [],
                        entry.interpolated_prompt_content.messages if entry.interpolated_prompt_content else [])

                    is_continued_conversation = all(x == y for x, y in zipped_messages)

                    if not is_continued_conversation:
                        session_groups.append(
                            self.__session_group_for_chat(entry, SessionEntryGroupType.Chain, evaluations, project_id))
                # Text chains
                else:
                    session_groups.append(SessionEntryGroup.from_entry(
                        entry,
                        SessionEntryGroupType.Chain,
                        evaluations,
                        project_id))
            elif is_continued_conversation:
                # Handle final entry of a conversation - record all chats.
                # We don't handle conversation evaluation yet.
                session_groups.append(self.__session_group_for_chat(entry, SessionEntryGroupType.Chat, [], project_id))
            else:
                # Subsequent non-chat sessions.
                session_groups.append(SessionEntryGroup.from_entry(
                    entry,
                    SessionEntryGroupType.Chain,
                    evaluations,
                    project_id))

            if next_entry and entry.template_name != next_entry.template_name:
                # If next entry is not the same base template, reset the conversation tracking state.
                is_continued_conversation = False

        return session_groups

    @staticmethod
    def __append_completion_response_to_continuous_chat(
            entry: ProjectSessionEntryDetailsRecord
    ) -> Optional[PromptModel]:
        # Assumption: The last message of a chat conversation will be an assistant response.
        # This method appends to the conversation history for rendering.
        content = entry.interpolated_prompt_content
        if content is None or content.messages is None:
            return None

        messages = deepcopy(content.messages) if content.messages else []
        messages.append(ChatMessage(role='assistant', content=entry.response))

        return PromptModel(messages)

    @staticmethod
    def __session_group_for_chat(
            entry: ProjectSessionEntryDetailsRecord,
            type: SessionEntryGroupType,
            evaluations: Evaluations,
            project_id: UUID,
    ) -> SessionEntryGroup:
        updated_content = SessionDisplayService.__append_completion_response_to_continuous_chat(entry)
        return SessionEntryGroup.from_entry(entry, type, evaluations, project_id, updated_content)

    @staticmethod
    def __get_multi_session_overview(session_details: ProjectSessionDetailsRecord) -> list[DisplayMetadataInfo]:
        metadata = []

        session_cost = ProjectSessionCalculator.calculate_costs(
            session_details.aggregate_prompt_token_cost, session_details.aggregate_return_token_cost)

        if session_cost:
            metadata.append(DisplayMetadataInfo("Total Session Cost", format_decimal_dollars(session_cost)))

        if session_details.aggregate_session_latency:
            metadata.append(
                DisplayMetadataInfo("Total Session Latency", f"{round(session_details.aggregate_session_latency, 1)}s"))
        return_token_count = session_details.aggregate_return_token_count
        prompt_token_count = session_details.aggregate_prompt_token_count
        if return_token_count and prompt_token_count:
            metadata.append(DisplayMetadataInfo("Total Tokens", f'{return_token_count + prompt_token_count:,}'))

        return metadata

    @staticmethod
    def __get_single_session_group_overview(
            session_details: ProjectSessionDetailsRecord,
            project_id: UUID
    ) -> list[DisplayMetadataInfo]:
        metadata = SessionDisplayService.__get_multi_session_overview(session_details)
        template_version_url = \
            f'/projects/{project_id}/templates/{session_details.entries[0].prompt_template_id}/versions/{session_details.entries[0].prompt_template_version_id}'

        metadata.append(DisplayMetadataInfo("Version", session_details.entries[0].template_name, template_version_url))
        metadata.append(DisplayMetadataInfo(
            "Provider",
            f"{session_details.entries[0].llm_provider} ({session_details.entries[0].llm_model})"))
        for param, value in session_details.entries[0].llm_parameters.items():
            if not param == 'functions':
                metadata.append(DisplayMetadataInfo(param, value))
        if session_details.entries[0].api_key_name:
            metadata.append(DisplayMetadataInfo(
                "API Key", session_details.entries[0].api_key_name))
        if session_details.entries[0].environment_name:
            metadata.append(
                DisplayMetadataInfo(
                    "Environment",
                    session_details.entries[0].environment_name,
                    is_env_deleted=session_details.entries[0].is_env_deleted
                )
            )

        return metadata

    def get_displayable_sessions(
            self,
            session_details: ProjectSessionDetailsRecord,
            evaluations: Evaluations,
            project_id: UUID,
    ) -> Tuple[list[SessionEntryGroup], list[DisplayMetadataInfo]]:
        session_groups = self.__fold_session_into_groups(session_details, evaluations, project_id)

        if len(session_groups) == 1:
            return session_groups, self.__get_single_session_group_overview(session_details, project_id)
        else:
            return session_groups, self.__get_multi_session_overview(session_details)

    def find_compatible_test_lists_for_session(
            self,
            session_details: ProjectSessionDetailsRecord,
            project_id: UUID
    ) -> list[TestListInfoWithSelection]:
        if len(session_details.entries) == 0:
            raise RuntimeError('Unexpected application state -- session without any session entries')

        test_lists = self.test_list_repo.find_all_by_project_id(project_id)

        compatible_test_lists = [test_list for test_list in test_lists if
                                 test_list.input_keys is None or
                                 set(test_list.input_keys) == set(session_details.entries[0].inputs.keys())]

        selected_test_list_ids = [test_list.id for test_list in
                                  self.test_list_repo.find_all_by_session_id(session_details.id)]

        return [TestListInfoWithSelection(TestListInfo(tl), tl.id in selected_test_list_ids) for tl in compatible_test_lists]

    def get_session_display_info(self, session_id: UUID) -> Optional[SessionDisplayInfo]:
        session_details = self.sessions_repo.try_find(session_id)
        if session_details is None:
            return None

        prompt_template_ids = [e.prompt_template_id for e in session_details.entries]

        evaluations: Evaluations = [
            (evaluation_criteria, evaluation_result)
            for evaluation_criteria, evaluation_result in sa.session.execute(
                evaluations_for_session(session_id, prompt_template_ids)
            ).all()
        ]

        test_lists = self.find_compatible_test_lists_for_session(session_details, g.project.id)
        sessions_for_display, session_overview = self.get_displayable_sessions(
            session_details, evaluations, g.project.id)
        first_timestamp = int(session_details.entries[0].logged_at.timestamp())

        return SessionDisplayInfo(
            created_at=first_timestamp,
            session_id=session_details.id,
            session_groups=sessions_for_display,
            session_overview=session_overview,
            evaluations=[(EvaluationCriteriaInfo(ec), EvaluationResultInfo(er) if er else None) for (ec, er) in
                         evaluations],
            test_lists=test_lists,
        )
