import json
from dataclasses import is_dataclass, asdict
from typing import Any
from ...JsonEncoder import Encoder


class DataclassEncoder(Encoder):
    @staticmethod
    def is_valid(element: Any) -> bool:
        return is_dataclass(element)

    @staticmethod
    def encode(element) -> dict:
        from ..DefaultJsonEncoder import DefaultJsonEncoder

        return json.loads(json.dumps(asdict(element), cls=DefaultJsonEncoder))
