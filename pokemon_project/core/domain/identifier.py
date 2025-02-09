from uuid import uuid4
from typing import Generic, TypeVar, Union

T = TypeVar("T", str, int)


class Identifier(Generic[T]):
    def __init__(self, value: Union[T, "Identifier[T]", None] = None):
        if isinstance(value, Identifier):
            self._value = value.toValue()
        elif isinstance(value, (str, int)):
            self._value = value
        elif value is None:
            self._value = str(uuid4())
        else:
            raise TypeError(
                f"Invalid value type: {type(value)}. Must be str, int, or Identifier."
            )

    def toValue(self):
        return self._value
