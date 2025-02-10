from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from core.domain.uniqueEntityId import UniqueEntityId

T = TypeVar("T")


class Entity(Generic[T], ABC):
    def __init__(self, props: T, id: UniqueEntityId | None = None):
        self._id = UniqueEntityId(id)
        self._props = props

    @property
    def id(self) -> UniqueEntityId:
        return self._id.toValue()

    @property
    def props(self) -> T:
        return self._props
