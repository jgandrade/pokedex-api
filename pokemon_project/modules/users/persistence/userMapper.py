from core.persistence.mapper import Mapper
from core.domain.uniqueEntityId import UniqueEntityId
from modules.users.domain.user import (
    User,
)
from modules.users.domain.models.user import UserModel


class UserMapper(Mapper):
    @staticmethod
    def toDomain(user_model: UserModel) -> User:
        return User.create(
            {
                "userId": user_model.user_id,
                "fullName": user_model.full_name,
                "userName": user_model.user_name,
                "email": user_model.email,
                "password": user_model.password,
                "profilePictureURL": user_model.profile_picture_url or "",
                "isEmailVerified": user_model.is_email_verified,
                "pokemonStoreId": user_model.pokemon_store_id or "",
                "createdAt": user_model.created_at.isoformat(),
                "updatedAt": user_model.updated_at.isoformat(),
            },
            user_model.id,
        )

    @staticmethod
    def toPersistence(user: User) -> UserModel:
        return UserModel(
            id=user.id,
            user_id=user.userId,
            full_name=user.fullName,
            user_name=user.userName,
            email=user.email,
            password=user.password,
            profile_picture_url=user.profilePictureURL,
            is_email_verified=user.isEmailVerified,
            pokemon_store_id=user.pokemonStoreId,
            created_at=user.createdAt,
            updated_at=user.updatedAt,
        )
