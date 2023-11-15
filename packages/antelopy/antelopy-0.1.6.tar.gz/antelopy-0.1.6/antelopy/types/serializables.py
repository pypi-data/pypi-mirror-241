from typing import Any, Dict, List, Protocol

from antelopy.types import serializers


class Serializable(Protocol):
    def serialize(self):
        ...

    def deserialize(self):
        ...


class BasicSerializer(Serializable):
    def __init__(self, value: Any, serialization_strategy: serializers.Serializer):
        self.value = value
        self.strategy = serialization_strategy

    def serialize(self):
        return self.strategy.serialize(self.value)

    def deserialize(self):
        return self.strategy.deserialize(self.value)


class ListSerializable(Serializable):
    def __init__(
        self, values: List[Serializable], serialization_strategy: serializers.Serializer
    ):
        self.values = values
        self.strategy = serialization_strategy

    def serialize(self):
        serialized_values = [v.serialize() for v in self.values]
        return self.strategy.serialize(serialized_values)

    def deserialize(self):
        return self.strategy.deserialize(self.values)


class DictSerializable(Serializable):
    def __init__(
        self,
        values: Dict[str, Serializable],
        serialization_strategy: serializers.Serializer,
    ):
        self.values = values
        self.strategy = serialization_strategy

    def serialize(self):
        return self.strategy.serialize(self.values)

    def deserialize(self):
        return self.strategy.deserialize(self.values)


SERIALIZER_MAP = {
    "name": serializers.NameSerializer(),
    "string": serializers.StringSerializer(),
    "uint8": serializers.NumberSerializer("uint8"),
    "int8": serializers.NumberSerializer("int8"),
}
