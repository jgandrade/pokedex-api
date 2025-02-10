from core.domain.aggregateRoot import AggregateRoot
from core.domain.uniqueEntityId import UniqueEntityId
from pydantic import BaseModel, Field
from typing import Union
from datetime import datetime, timezone


class UserProps(BaseModel):
    userId: str
    fullName: str
    userName: str
    email: str
    password: str
    profilePictureURL: str | None = None
    isEmailVerified: bool = False
    pokemonStoreId: str | None = None
    createdAt: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    updatedAt: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


class User(AggregateRoot):
    props: UserProps

    @staticmethod
    def create(props: dict, id: Union[UniqueEntityId, str, int, None] = None):
        user_props = UserProps(**props)
        return User(user_props, id)

    @staticmethod
    def createWithDefaults(props: dict):
        default_props = {
            "userId": UniqueEntityId(None).toValue(),
            "profilePictureURL": None,
            "isEmailVerified": False,
            "pokemonStoreId": None,
            "createdAt": datetime.now(timezone.utc).isoformat(),
            "updatedAt": datetime.now(timezone.utc).isoformat(),
        }
        merged_props = {**default_props, **props}
        
        return User.create(merged_props)

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
