from datetime import datetime
from typing import Any

from ...JsonEncoder.Encoder import Encoder


class DatetimeEncoder(Encoder):
    @staticmethod
    def is_valid(element: Any) -> bool:
        return isinstance(element, datetime)

    @staticmethod
    def encode(element: datetime) -> str:
        return str(element.timestamp())
