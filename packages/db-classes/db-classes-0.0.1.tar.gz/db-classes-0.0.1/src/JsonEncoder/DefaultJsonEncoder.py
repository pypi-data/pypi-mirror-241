from json import JSONEncoder

from .Encoder import Encoder


class DefaultJsonEncoder(JSONEncoder):
    def default(self, obj):
        for encoder in Encoder.__subclasses__():
            if encoder.is_valid(obj):
                return encoder.encode(obj)
        else:
            raise ValueError(f"{obj=} can't be encoded")
