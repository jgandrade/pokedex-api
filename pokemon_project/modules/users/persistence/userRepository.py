from pokemon_project.core.persistence.repository import Repository
from pokemon_project.modules.users.domain.user import User
from pokemon_project.modules.users.persistence.userMapper import UserMapper
from pokemon_project.modules.users.domain.models.user import UserModel
from pokemon_project.core.domain.uniqueEntityId import UniqueEntityId


class UserRepository(Repository):
    def save(self, user: User) -> None:
        user_model = UserMapper.toPersistence(user)
        user_model.save()

    def findById(self, user_id: UniqueEntityId) -> User | None:
        try:
            user_model = UserModel.objects.get(user_id=user_id.toValue())
            return UserMapper.toDomain(user_model)
        except UserModel.DoesNotExist:
            return None

    def findByEmail(self, email: str) -> User | None:
        try:
            user_model = UserModel.objects.get(email=email)
            return UserMapper.toDomain(user_model)
        except UserModel.DoesNotExist:
            return None

    def delete(self, user: User) -> None:
        user_model = UserMapper.toPersistence(user)
        user_model.delete()
