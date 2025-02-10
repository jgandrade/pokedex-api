from pokemon_project.core.infrastructure.baseController import BaseController
from pokemon_project.modules.users.use_cases.user.findByIdUseCase import (
    UserFindByIdUseCase,
)


class UserController(BaseController):

    def __init__(self, find_by_id_use_case=UserFindByIdUseCase()):
        self._findByIdUseCase = find_by_id_use_case

    def findById(self, id: str):
        user_domain_result = self._findByIdUseCase(id)

        return user_domain_result
