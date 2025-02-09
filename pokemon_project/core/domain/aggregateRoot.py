from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from pokemon_project.core.domain.entity import Entity

T = TypeVar("T")


class AggregateRoot(Entity, Generic[T], ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def createWithDefaults(self):
        pass
