from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class BaseController(Generic[T], ABC):

    @abstractmethod
    def findById(self):
        pass
