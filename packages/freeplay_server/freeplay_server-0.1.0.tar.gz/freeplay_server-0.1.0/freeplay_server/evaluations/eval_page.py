from dataclasses import dataclass
from enum import StrEnum
from typing import Optional, Union
from uuid import UUID

from freeplay_server.models import EvaluationCriteria, EvaluationResult

ONE_TO_FIVE_EVALUATION_CRITERIA_OPTIONS: list[int] = [1, 2, 3, 4, 5]
YES_NO_EVALUATION_CRITERIA_OPTIONS: list[str] = ['no', 'yes']


class EvalCriteriaType(StrEnum):
    OneToFive = '1-5'
    YesNo = 'yes-no'


@dataclass
class EvaluationResultInfo:
    auto_eval_score: Optional[str]
    manual_score: Optional[str]

    def __init__(self, result: EvaluationResult):
        self.auto_eval_score = result.auto_eval_score
        self.manual_score = result.manual_score


@dataclass
class EvaluationCriteriaInfo:
    id: UUID
    name: str
    question: str
    llm_question: str
    llm_eval_enabled: bool
    type: EvalCriteriaType
    options: Union[list[str], list[int]]
    rubric: dict[str, str]

    def __init__(self, criterion: EvaluationCriteria):
        self.id = criterion.id
        self.name = criterion.name
        self.question = criterion.question
        self.llm_question = criterion.llm_question
        self.llm_eval_enabled = criterion.llm_eval_enabled
        criteria_type = EvalCriteriaType(criterion.type)
        self.type = criteria_type
        self.options = self.options_for_type(criteria_type)
        self.rubric = {str(r.score): r.instructions for r in criterion.rubric}

    @staticmethod
    def options_for_type(eval_criteria_type: EvalCriteriaType) -> Union[list[str], list[int]]:
        match eval_criteria_type:
            case EvalCriteriaType.OneToFive:
                return ONE_TO_FIVE_EVALUATION_CRITERIA_OPTIONS
            case EvalCriteriaType.YesNo:
                return YES_NO_EVALUATION_CRITERIA_OPTIONS
            case _:
                raise ValueError('Unexpected Evaluation Criteria Type')
