from typing import Callable

from log_module import LoggerSingleton
from regular_calc import RegularCalculator

logger = LoggerSingleton()


def logging_on_start_and_finish(function_for_decorate: Callable):
    def wrapper():
        logger.log(f"function {function_for_decorate} start")
        function_for_decorate()
        logger.log(f"function {function_for_decorate} end")

    return wrapper


@logging_on_start_and_finish
def main():
    calculator = RegularCalculator()

    print(calculator.calc("+", 2, 2, 2))


if __name__ == "__main__":
    main()
