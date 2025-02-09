from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Mapper(Generic[T], ABC):
    @abstractmethod
    def toPersistence(self):
        pass

    @abstractmethod
    def toDomain(self):
        pass
