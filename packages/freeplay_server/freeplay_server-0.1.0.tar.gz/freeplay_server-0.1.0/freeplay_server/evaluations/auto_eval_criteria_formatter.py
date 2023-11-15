import dataclasses
import re
from dataclasses import dataclass
from re import Match
from typing import Optional, Union

from freeplay_server.evaluations.auto_eval_errors import AutoEvalTemplatingError
from freeplay_server.web_support import json_support

NestedDict = dict[str, Union[str, 'NestedDict']]


@dataclass
class EvaluationCriteriaFunctionCall:
    name: str
    arguments: dict[str, str]

    def __init__(self, name: str, arguments: str):
        self.name = name
        self.arguments = json_support.as_dict(arguments)


@dataclass
class EvaluationCriteriaSessionInfo:
    function_call: Optional[EvaluationCriteriaFunctionCall]
    output: Optional[str]
    inputs: dict[str, str]


class AutoEvalCriteriaFormatter:
    # Extract arbitrarily nested variables with `.` object notation within {{variables}}
    TemplatePattern = r'\{\{(\w+(?:\.\w+)*)\}\}'

    @staticmethod
    def format(auto_eval_criteria_definition: str, auto_eval_data: EvaluationCriteriaSessionInfo) -> str:
        # Formats an auto eval criteria and a set of hydrated evaluation data into
        # an executable auto evaluation LLM request
        # "Is the input <input>{{inputs.variable_name}}</input> in the same language as <output>{{output}}</output>
        return re.sub(
            AutoEvalCriteriaFormatter.TemplatePattern,
            lambda match: AutoEvalCriteriaFormatter.__interpolate_nested_dictionary_fields(
                dataclasses.asdict(auto_eval_data), match
            ),
            auto_eval_criteria_definition
        )

    @staticmethod
    def __get_template_field_value_from_data(
            data_lookup_dict: NestedDict,
            attribute_names: list[str]
    ) -> Optional[str]:
        field_value = data_lookup_dict.get(attribute_names[0])
        if type(field_value) is dict:
            return AutoEvalCriteriaFormatter.__get_template_field_value_from_data(field_value, attribute_names[1:])
        elif type(field_value) is str:
            return field_value

        return None

    @staticmethod
    def __interpolate_nested_dictionary_fields(auto_eval_data: NestedDict, regex_match: Match[str]) -> str:
        maybe_nested_variable_name = regex_match.group(1)
        variable_attribute_names = maybe_nested_variable_name.split('.')
        value = AutoEvalCriteriaFormatter.__get_template_field_value_from_data(
            auto_eval_data, variable_attribute_names)

        if value is None:
            raise AutoEvalTemplatingError(
                f'Session data did not include evaluation criteria variable: {maybe_nested_variable_name}')

        return value
