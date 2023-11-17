import json
import sys
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from src import DbClass
from src import DbClassLiteral


def test_serialize_literal():
    @dataclass
    class Bar(DbClassLiteral):
        dictionary: dict
        date: datetime
        decimal: Decimal

    @dataclass
    class Foo(DbClass):
        dictionary: dict
        date: datetime
        decimal: Decimal
        bar: Bar

    foo = Foo({}, datetime.now(), Decimal(1), Bar({}, datetime.now(), Decimal(1)))
    serialized = foo.get_db_representation()
    try:
        json.dump(serialized, sys.stdout)
    except:
        assert False
    deserialized = Foo.from_dict(serialized)
    assert deserialized == foo


def test_serialize():
    @dataclass
    class Bar(DbClass):
        dictionary: dict
        date: datetime
        decimal: Decimal

    @dataclass
    class Foo(DbClass):
        dictionary: dict
        date: datetime
        decimal: Decimal
        bar: Bar

    foo = Foo({}, datetime.now(), Decimal(1), Bar({}, datetime.now(), Decimal(1)))
    serialized = foo.get_db_representation()
    foo.bar = foo.bar._id
    try:
        json.dump(serialized, sys.stdout)
    except:
        assert False
    deserialized = Foo.from_dict(serialized)
    assert deserialized == foo


if __name__ == "__main__":
    test_serialize_literal()
    test_serialize()
