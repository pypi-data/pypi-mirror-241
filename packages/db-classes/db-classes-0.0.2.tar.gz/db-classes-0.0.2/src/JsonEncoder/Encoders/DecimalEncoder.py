from decimal import Decimal
from typing import Any

from ...JsonEncoder.Encoder import Encoder


class DecimalEncoder(Encoder):
    @staticmethod
    def is_valid(element: Any) -> bool:
        return isinstance(element, Decimal)

    @staticmethod
    def encode(element: Decimal) -> str:
        return str(element)
