from pokemon_project.core.domain.useCase import UseCase
from pokemon_project.modules.users.persistence.userRepository import UserRepository


class UserFindByIdUseCase(UseCase):

    def __init__(self, user_repository=UserRepository()):
        self._userRepository = user_repository

    def execute(self):
        return "test"
