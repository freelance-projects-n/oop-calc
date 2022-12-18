from abc import abstractmethod, ABC


class AbstractCalculator(ABC):
    @abstractmethod
    def calc(self,
             operation: str,
             input_numbers: list[float]):
        pass


class NotSupportedMethodError(Exception):
    pass
