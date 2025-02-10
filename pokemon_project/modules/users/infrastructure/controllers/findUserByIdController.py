from core.infrastructure.baseController import BaseController
from modules.users.use_cases.user.findByIdUseCase import (
    UserFindByIdUseCase,
)
from modules.users.infrastructure.decorators.requireJWT import require_jwt


class FindUserByIdController(BaseController):

    def __init__(self, find_by_id_use_case=UserFindByIdUseCase(), **kwargs):
        super().__init__(**kwargs)
        self._findByIdUseCase = find_by_id_use_case

    @require_jwt
    def get(self, request, id: str):
        user_domain_result = self._findByIdUseCase.execute(id)

        if not user_domain_result:
            return self.not_found("User not found")

        return self.json_response(user_domain_result)
