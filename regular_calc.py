from enum import Enum
from typing import Callable

from abstract_calc import AbstractCalculator, NotSupportedMethodError


class RegularOperations(str, Enum):
    addition = "+"
    subtraction = "-"
    multiplication = "*"
    exponentiation = "**"
    division = "/"
    integer_division = "//"
    remainder_of_division = "%"


class RegularCalculator(AbstractCalculator):
    def calc(self,
             operation: RegularOperations,
             *input_numbers: float):

        output = input_numbers[0]
        method_for_calc = self._get_method_for_calc(operation)

        for number_index in range(1, len(input_numbers)):
            output = method_for_calc(output, input_numbers[number_index])

        return output

    @staticmethod
    def _get_method_for_calc(operation: RegularOperations) -> Callable[[float,
                                                                        float],
                                                                       float]:
        if operation == RegularOperations.addition:
            return lambda a, b: a + b

        elif operation == RegularOperations.subtraction:
            return lambda a, b: a - b

        elif operation == RegularOperations.multiplication:
            return lambda a, b: a * b

        elif operation == RegularOperations.exponentiation:
            return lambda a, b: a ** b

        elif operation == RegularOperations.division:
            return lambda a, b: a / b

        elif operation == RegularOperations.integer_division:
            return lambda a, b: a // b

        elif operation == RegularOperations.remainder_of_division:
            return lambda a, b: a % b

        else:
            raise NotSupportedMethodError()
