import logging
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any
from uuid import UUID

from dacite import WrongTypeError
from flask import Blueprint, Response, request, g
from flask.typing import ResponseReturnValue
from sqlalchemy import select

from freeplay_server.auth.auth_filter import api_endpoint
from freeplay_server.evaluations.auto_eval_processor import AutoEvalProcessor, AutoEvalFields, AutoEvalFunctionResponse
from freeplay_server.extensions import sa
from freeplay_server.models import Environment
from freeplay_server.project_sessions.project_sessions_repository import FunctionCall
from freeplay_server.prompt_templates.llm_model_parameters import UnexpectedParameterError
from freeplay_server.record.session_recorder import SessionRecorder
from freeplay_server.web_support import json_support, api_support

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class RecordPayload:
    session_id: UUID
    project_version_id: UUID  # hack -- old SDKs send prompt_template_version_id with this field TODO: ENG-547
    prompt_template_id: UUID
    start_time: float
    end_time: float
    tag: str
    inputs: dict[str, str]
    prompt_content: str
    return_content: str
    format_type: str
    is_complete: bool
    test_run_id: Optional[UUID]
    model: Optional[str] = None
    provider: Optional[str] = None
    llm_parameters: Optional[dict[str, Any]] = None
    function_call_response: Optional[FunctionCall] = None
    prompt_template_version_id: Optional[UUID] = None
    project_id: Optional[UUID] = None


def record_api(
        recorder: SessionRecorder,
        auto_eval_processor: AutoEvalProcessor
) -> Blueprint:
    api = Blueprint('record_api', __name__)

    @api_endpoint
    @api.post('/api/v1/record')
    def record() -> ResponseReturnValue:
        try:
            record_payload = json_support.force_decode(RecordPayload, request.data)
        except WrongTypeError as e:
            return api_support.api_bad_request(f'Unable to parse request body. Wrong type for field {e.field_path}.')
        except Exception:
            return api_support.api_bad_request(f'Unable to parse request body')

        llm_parameters = record_payload.llm_parameters if record_payload.llm_parameters else {}

        # TODO ENG-867 -- Remove these timezone corrections once customer SDKs are updated.
        try:
            # The JVM SDK incorrectly published JVM times in 1970. We need to correct for these times by logging
            # a relative timestamp based on the (correct) recorded latency starting from "now".
            recorded_start_time = datetime.fromtimestamp(record_payload.start_time)
            recorded_end_time = datetime.fromtimestamp(record_payload.end_time)

            if recorded_start_time.year < 2023:
                start_time = datetime.now()
                session_entry_latency = (recorded_end_time - recorded_start_time)
                end_time = start_time + session_entry_latency
            else:
                start_time = recorded_start_time
                end_time = recorded_end_time

        except ValueError:
            # SDKs are expected to send start and end times as a float - old versions may pass them as epoch millis.
            # This code compensates by setting start and end times to None in the case the published times don't make sense.
            logger.warning('Received start_time or end_time out of expected values. SDK version may be out of date.')
            start_time = datetime.now()
            end_time = None

        authorization_header = request.headers.get('Authorization')
        if authorization_header and authorization_header.startswith('Bearer '):
            api_key_last_four = str(authorization_header.split(' ')[1])[-4:]
        account_id = g.account.id

        query = (
            select(Environment.id)
            .where(Environment.name == record_payload.tag)
        )
        environment_id = sa.session.execute(query).scalar_one()

        try:
            recorder.record(
                session_id=record_payload.session_id,
                prompt_template_id=record_payload.prompt_template_id,
                # Note: this field actually represents the prompt_template_version_id -- the value is correct but
                # the field remains for backwards compatibility. TODO: ENG-547
                prompt_template_version_id=record_payload.prompt_template_version_id or record_payload.project_version_id,
                tag=record_payload.tag,
                inputs=record_payload.inputs,
                llm_parameters=llm_parameters,
                prompt_content=record_payload.prompt_content,
                return_content=record_payload.return_content,
                format_type=record_payload.format_type,
                is_complete=record_payload.is_complete,
                test_run_id=record_payload.test_run_id,
                model=record_payload.model,
                provider=record_payload.provider,
                start_time=start_time,
                end_time=end_time,
                function_call_response=record_payload.function_call_response,
                project_id=record_payload.project_id,
                api_key_last_four=api_key_last_four,
                account_id=account_id,
                environment_id=environment_id,
            )
            if record_payload.test_run_id:
                auto_eval_fields = AutoEvalFields(
                    prompt_template_id=record_payload.prompt_template_id,
                    inputs=record_payload.inputs,
                    output=record_payload.return_content,
                    function_call_response=AutoEvalFunctionResponse(
                        record_payload.function_call_response.name,
                        record_payload.function_call_response.arguments
                    ) if record_payload.function_call_response else None,
                    session_id=record_payload.session_id
                )
                auto_eval_processor.process(auto_eval_fields)

        except UnexpectedParameterError as e:
            return api_support.api_bad_request(str(e))

        return Response(status=201)

    return api
