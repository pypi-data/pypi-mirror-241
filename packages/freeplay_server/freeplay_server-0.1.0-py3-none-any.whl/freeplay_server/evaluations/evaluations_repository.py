import uuid
from operator import and_

from sqlalchemy import Select, select

from freeplay_server.models import EvaluationCriteria, EvaluationResult


def evaluations_for_session(session_id: uuid.UUID, prompt_template_ids: list[uuid.UUID]) -> Select[
    tuple[EvaluationCriteria, EvaluationResult]]:
    return (select(EvaluationCriteria, EvaluationResult)
    .outerjoin(
        EvaluationResult,
        and_(
            EvaluationCriteria.id == EvaluationResult.evaluation_criteria_id,
            EvaluationResult.session_id == session_id
        )
    ).where(
        EvaluationCriteria.prompt_template_id.in_(prompt_template_ids),
    ))
