from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any
from uuid import UUID

from freeplay_server.database_support.database_gateway import DatabaseGateway
from freeplay_server.project_sessions.project_sessions_repository import FunctionCall, ProjectSessionsRepository
from freeplay_server.record.session_cost_calculator import SessionCostCalculator
from freeplay_server.record.token_counting import TokenCounting


@dataclass(frozen=True)
class SessionRecord:
    id: UUID
    prompt_template_id: Optional[UUID]
    project_version_id: Optional[UUID]
    tag: str
    session_id: Optional[UUID]
    request_id: Optional[UUID]
    response_id: Optional[UUID]
    test_run_id: Optional[UUID]
    created_at: datetime


class SessionRecorder:
    def __init__(self, db: DatabaseGateway, project_sessions_repository: ProjectSessionsRepository, ) -> None:
        self.db = db
        self.project_sessions_repository = project_sessions_repository
        self.token_counting = TokenCounting()
        self.cost_calculator = SessionCostCalculator()

    def record(self,
               session_id: UUID,
               prompt_template_id: UUID,
               prompt_template_version_id: UUID,
               tag: str,
               inputs: dict[str, str],
               llm_parameters: dict[str, Any],
               prompt_content: str,
               return_content: str,
               format_type: str,
               is_complete: bool,
               api_key_last_four: str,
               account_id: UUID,
               test_run_id: Optional[UUID],
               model: Optional[str],
               provider: Optional[str],
               start_time: datetime,
               end_time: Optional[datetime],
               function_call_response: Optional[FunctionCall],
               project_id: Optional[UUID],
               environment_id: Optional[UUID],
               ) -> None:
        token_counts = self.token_counting.count_tokens(
            model, prompt_content, return_content) if model is not None else None
        prompt_costs = self.cost_calculator.calculate_cost(
            model, token_counts) if model is not None and token_counts is not None else None

        with self.db.transaction() as connection:
            self.project_sessions_repository.save_direct(
                connection,
                session_id=session_id,
                prompt_template_version_id=prompt_template_version_id,
                prompt_template_id=prompt_template_id,
                inputs=inputs,
                llm_parameters=llm_parameters,
                prompt_content=prompt_content,
                return_content=return_content,
                prompt_token_count=token_counts.prompt_token_count if token_counts else None,
                return_token_count=token_counts.return_token_count if token_counts else None,
                prompt_token_cost=prompt_costs.prompt_token_cost if prompt_costs else None,
                return_token_cost=prompt_costs.return_token_cost if prompt_costs else None,
                format_type=format_type,
                is_complete=is_complete,
                logged_at=datetime.now(),
                test_run_id=test_run_id,
                model=model,
                provider=provider,
                start_time=start_time,
                end_time=end_time,
                function_call_response=function_call_response,
                project_id=project_id,
                api_key_last_four=api_key_last_four,
                account_id=account_id,
                environment_id=environment_id,
            )
