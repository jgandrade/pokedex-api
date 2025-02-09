from pokemon_project.core.domain.aggregateRoot import AggregateRoot
from pokemon_project.core.domain.uniqueEntityId import UniqueEntityId
from pydantic import BaseModel
from typing import Union


class UserProps(BaseModel):
    userId: str
    fullName: str
    userName: str
    email: str
    password: str
    profilePictureURL: str
    isEmailVerified: bool
    pokemonStoreId: str
    createdAt: str
    updatedAt: str


class User(AggregateRoot):
    props: UserProps

    @staticmethod
    def create(props: dict, id: Union[UniqueEntityId, str, int, None] = None):
        user_props = UserProps(**props)
        return User(user_props, id)

    @staticmethod
    def createWithDefaults(id: Union[UniqueEntityId, str, int, None] = None):
        return User(UserProps(name="Default", age=0), id)

    @property
    def userId(self) -> str:
        return self.props.userId

    @property
    def fullName(self) -> str:
        return self.props.fullName

    @property
    def userName(self) -> str:
        return self.props.userName

    @property
    def email(self) -> str:
        return self.props.email

    @property
    def password(self) -> str:
        return self.props.password

    @property
    def profilePictureURL(self) -> str:
        return self.props.profilePictureURL

    @property
    def isEmailVerified(self) -> bool:
        return self.props.isEmailVerified

    @property
    def pokemonStoreId(self) -> str:
        return self.props.pokemonStoreId

    @property
    def createdAt(self) -> str:
        return self.props.createdAt

    @property
    def updatedAt(self) -> str:
        return self.props.updatedAt
