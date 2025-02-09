from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Repository(Generic[T], ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def findById(self):
        pass
