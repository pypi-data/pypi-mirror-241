import atexit
import logging
from dataclasses import dataclass
from enum import Enum
from multiprocessing.pool import ThreadPool, ApplyResult
from typing import Union, Optional, Any
from uuid import UUID

from freeplay import Freeplay
from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker, scoped_session, joinedload
from sqlalchemy.orm.scoping import ScopedSession

from freeplay_server.app_environment import AutoEvalFreeplayConfig
from freeplay_server.evaluations.auto_eval_criteria_formatter import AutoEvalCriteriaFormatter, \
    EvaluationCriteriaSessionInfo, EvaluationCriteriaFunctionCall
from freeplay_server.models import EvaluationCriteria, EvaluationResult
from freeplay_server.monitoring.datadog_client import DatadogClient, FreeplayMetric

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class AutoEvalFunctionResponse:
    name: str
    arguments: str


@dataclass(frozen=True)
class AutoEvalFields:
    prompt_template_id: UUID
    function_call_response: Optional[AutoEvalFunctionResponse]
    inputs: dict[str, str]
    output: str
    session_id: UUID


class AutoEvalProcessorResult(Enum):
    SUCCESS = 0
    FAILED = 1


class SingleAutoEvalResult(Enum):
    SUCCESS = 0
    FAILED = 1


# Note: Do not depend on Flask (Flask session, sql_alchemy app context, etc.) here. This behavior will be ported to
# a separate process outside Flask.
AUTO_EVAL_THREAD_POOL_SIZE = 4


class AutoEvalMetrics(FreeplayMetric):
    SessionsCount = 'freeplay.auto_evals.sessions'
    SessionsSuccess = 'freeplay.auto_evals.sessions.success'
    CriteriaCount = 'freeplay.auto_evals.criteria'
    CriteriaSuccess = 'freeplay.auto_evals.criteria.success'
    CriteriaFailureNormalization = 'freeplay.auto_evals.criteria.failure.normalization'
    CriteriaFailureExceptions = 'freeplay.auto_evals.criteria.failure.exceptions'


class AutoEvalProcessor:
    def __init__(
            self,
            db_engine: Engine,
            freeplay_client: Freeplay,
            freeplay_config: AutoEvalFreeplayConfig,
            datadog_client: DatadogClient):
        self.db_engine = db_engine
        self.session_maker = sessionmaker(db_engine)
        self.freeplay_client = freeplay_client
        self.freeplay_config = freeplay_config
        self.datadog_client = datadog_client
        self.thread_pool = ThreadPool(AUTO_EVAL_THREAD_POOL_SIZE)
        atexit.register(self.thread_pool.close)

    def process(
            self,
            auto_eval_fields: AutoEvalFields
    ) -> Optional[ApplyResult[AutoEvalProcessorResult]]:
        with self.session_maker() as session:
            auto_eval_criteria = session.query(
                EvaluationCriteria
            ).options(
                joinedload(EvaluationCriteria.rubric)
            ).where(
                EvaluationCriteria.prompt_template_id == auto_eval_fields.prompt_template_id,
                EvaluationCriteria.llm_eval_enabled
            ).all()
            for criterion in auto_eval_criteria:
                # Disconnect the criteria objects from the sql alchemy session
                # so they can be safely used outside the scope of the session.
                session.expunge(criterion)

        if auto_eval_criteria:
            # Processes all criteria for a single session in one thread.
            return self.thread_pool.apply_async(
                self.__process_auto_evals_for_session,
                (auto_eval_criteria, auto_eval_fields))

        return None

    def __process_auto_evals_for_session(
            self,
            evaluation_criteria: list[EvaluationCriteria],
            auto_eval_fields: AutoEvalFields
    ) -> AutoEvalProcessorResult:
        logger.info("Starting auto-eval in thread pool")
        self.datadog_client.increment(AutoEvalMetrics.SessionsCount)

        threadsafe_session_factory = scoped_session(sessionmaker(bind=self.db_engine))
        try:
            results = [self.__process_single_auto_eval(
                criterion, auto_eval_fields, threadsafe_session_factory
            ) for criterion in evaluation_criteria]

            if SingleAutoEvalResult.FAILED in results:
                return AutoEvalProcessorResult.FAILED
            else:
                self.datadog_client.increment(AutoEvalMetrics.SessionsSuccess)
                return AutoEvalProcessorResult.SUCCESS
        except Exception:
            logger.exception(f'Exception running auto eval worker. Dropping auto eval.')
            self.datadog_client.increment(AutoEvalMetrics.CriteriaFailureExceptions)
            return AutoEvalProcessorResult.FAILED
        finally:
            # Manually clean up session before thread completes.
            threadsafe_session_factory.remove()

    def __process_single_auto_eval(
            self,
            criterion: EvaluationCriteria,
            auto_eval_fields: AutoEvalFields,
            threadsafe_session_factory: ScopedSession[Any]
    ) -> SingleAutoEvalResult:
        logger.info(f"Processing auto-eval criterion: {criterion.id}")
        self.datadog_client.increment(AutoEvalMetrics.CriteriaCount)

        formatted_llm_question = AutoEvalCriteriaFormatter.format(
            criterion.llm_question,
            EvaluationCriteriaSessionInfo(
                function_call=EvaluationCriteriaFunctionCall(
                    auto_eval_fields.function_call_response.name,
                    auto_eval_fields.function_call_response.arguments
                ) if auto_eval_fields.function_call_response else None,
                output=auto_eval_fields.output,
                inputs=auto_eval_fields.inputs
            ))

        formatted_rubric = "\n".join([f"{r.score}: {r.instructions}" for r in criterion.rubric])

        completion = self.freeplay_client.get_completion(
            project_id=self.freeplay_config.project_id,
            template_name=self.freeplay_config.template_name,
            variables={
                "llm_question": formatted_llm_question,
                "scale": criterion.type,
                "rubric": formatted_rubric,
            },
            tag=self.freeplay_config.template_environment,
        )

        logger.info("Successfully received completion from OpenAI")

        normalized_score = AutoEvalProcessor.__normalize_openai_auto_eval_result(completion.content)

        if not normalized_score:
            logger.info(
                f'Failed to normalize auto eval score from OpenAI: `{completion.content}`. Dropping auto eval.')
            self.datadog_client.increment(AutoEvalMetrics.CriteriaFailureNormalization)
            return SingleAutoEvalResult.FAILED

        with threadsafe_session_factory() as session:
            session.add(EvaluationResult(
                session_id=auto_eval_fields.session_id,
                evaluation_criteria_id=criterion.id,
                auto_eval_score=normalized_score))
            session.commit()

        logger.info(f"Successfully processed and stored auto-eval for criterion: {criterion.id}")
        self.datadog_client.increment(AutoEvalMetrics.CriteriaSuccess)
        return SingleAutoEvalResult.SUCCESS

    @staticmethod
    def __normalize_openai_auto_eval_result(content: str) -> Optional[Union[str, int]]:
        # Only 1-5, yes, and no are valid responses for an auto-eval. Otherwise, the eval will be dropped.
        try:
            if content.isdigit():
                return int(content)
            else:
                lowercase_value = content.lower()
                if lowercase_value != 'yes' and lowercase_value != 'no':
                    return None
                else:
                    return lowercase_value
        except RuntimeError:
            return None
