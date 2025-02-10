from core.domain.useCase import UseCase
from modules.users.domain.user import User
from modules.users.persistence.userRepository import UserRepository


class UserFindByIdUseCase(UseCase):

    def __init__(self, user_repository=UserRepository()):
        self._userRepository = user_repository

    def execute(self, id: str | int | None = None) -> dict:
        user_domain = self._userRepository.findById(id)

        return user_domain
