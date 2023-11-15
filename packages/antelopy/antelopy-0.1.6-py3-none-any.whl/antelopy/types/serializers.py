import struct
from typing import Any, Protocol, Tuple, Union

from antelopy.serializers import names, varints
from antelopy.types.types import DEFAULT_TYPES


class Serializer(Protocol):
    """Base Serializer Protocol"""

    def serialize(self, v: Any) -> Any:
        ...

    def deserialize(self, v: Any) -> Any:
        ...


class NameSerializer(Serializer):
    def serialize(self, v: str) -> bytes:
        return names.serialize_name(v)

    def deserialize(self, v: bytes) -> str:
        return names.deserialize_name(v)


class NumberSerializer(Serializer):
    def __init__(self, type: str):
        self.type = type

    def serialize(self, n: Union[int, float]) -> bytes:
        return struct.pack(DEFAULT_TYPES[self.type], n)

    def deserialize(self, v: bytes) -> str:
        ...


class StringSerializer(Serializer):
    def serialize(self, v: str) -> bytes:
        return VaruintSerializer().serialize(len(v)) + v.encode("utf-8")

    def deserialize(self, v: Any) -> Any:
        ...


class VarintSerializer(Serializer):
    def serialize(self, v: int) -> bytes:
        return varints.serialize_varint((v << 1) ^ (v >> 31))

    def deserialize(self, v: bytes) -> Tuple[int, bytes]:
        return varints.deserialize_varint(v)


class VaruintSerializer(Serializer):
    def serialize(self, v: int) -> bytes:
        return varints.serialize_varint(v)

    def deserialize(self, v: bytes) -> Tuple[int, bytes]:
        return varints.deserialize_varint(v)
