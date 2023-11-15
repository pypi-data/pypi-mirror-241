from dataclasses import dataclass
from enum import StrEnum
from typing import Union


class UnexpectedParameterError(Exception):
    pass


class UnexpectedResultError(Exception):
    pass


class LLMModelParameterType(StrEnum):
    String = 'string'
    Integer = 'integer'
    Float = 'float'


LLMModelParameterValue = Union[str, int, float]


def parse_model_parameter_from_string(
        parameter_type: LLMModelParameterType,
        parameter_str_value: str
) -> LLMModelParameterValue:
    try:
        match parameter_type:
            case LLMModelParameterType.String:
                return parameter_str_value
            case LLMModelParameterType.Integer:
                return int(parameter_str_value)
            case LLMModelParameterType.Float:
                return float(parameter_str_value)
            case _:
                raise UnexpectedParameterError(f"Unexpected parameter type: {parameter_type}")
    except ValueError as e:
        raise UnexpectedParameterError(
            f"Parameter value: {parameter_str_value} could not be parsed as type: {parameter_type}")


@dataclass
class LLMModelParameter:
    name: str
    type: LLMModelParameterType
    value: LLMModelParameterValue

    def __init__(
            self,
            name: str,
            type: LLMModelParameterType,
            value: str
    ):
        self.name = name
        self.type = type
        self.value = parse_model_parameter_from_string(type, value)
