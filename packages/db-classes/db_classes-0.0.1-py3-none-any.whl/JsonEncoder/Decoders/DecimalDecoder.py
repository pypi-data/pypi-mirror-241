from decimal import Decimal
from typing import Any

from ...JsonEncoder import Decoder


class DecimalDecoder(Decoder):
    @staticmethod
    def is_valid(element: Any) -> bool:
        return element == Decimal

    @staticmethod
    def decode(element: Any) -> Decimal:
        return Decimal(element)
