import json
import random
from typing import Any, Self

from dataclasses import dataclass, field, fields

from dacite import from_dict, Config

from .JsonEncoder import Decoder
from .JsonEncoder import DefaultJsonEncoder


@dataclass
class DbClass:
    _id: Any = field(init=False, default_factory=lambda: random.randint(0, 2**64))
    json_encoder = DefaultJsonEncoder

    def __post_init__(self):
        self._decode()

    def get_db_representation(self) -> dict:
        from .DbClassLiteral import DbClassLiteral

        return json.loads(
            json.dumps(
                dict(
                    (
                        f.name,
                        value._id
                        if isinstance(value := getattr(self, f.name), DbClass)
                        and not isinstance(value, DbClassLiteral)
                        else value,
                    )
                    for f in fields(self)
                ),
                cls=self.json_encoder,
            )
        )

    @classmethod
    def from_dict(cls, dictionary: dict) -> Self:
        return from_dict(cls, dictionary, Config(check_types=False))

    def _decode(self):
        for f in fields(self):
            for decoder in Decoder.__subclasses__():
                if decoder.is_valid(f.type):
                    setattr(self, f.name, decoder.decode(getattr(self, f.name)))
                    break
