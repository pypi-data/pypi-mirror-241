from abc import abstractmethod
from typing import Any
from ..JsonEncoder.JsonOperator import JSONOperator


class Encoder(JSONOperator):
    @staticmethod
    @abstractmethod
    def is_valid(element: Any) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def encode(element: Any) -> str:
        pass
