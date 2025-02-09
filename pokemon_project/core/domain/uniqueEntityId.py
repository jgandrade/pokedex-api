from uuid import uuid4
from pokemon_project.core.domain.identifier import Identifier
from typing import Union


class UniqueEntityId(Identifier[str]):
    def __init__(self, id: Union[str, Identifier[str], None] = None):
        super().__init__(id)
