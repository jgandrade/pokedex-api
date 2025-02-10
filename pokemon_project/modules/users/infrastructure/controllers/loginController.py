from core.infrastructure.baseController import BaseController
from modules.users.use_cases.user.loginUseCase import UserLoginUseCase


class UserLoginController(BaseController):
    def __init__(self, login_use_case=UserLoginUseCase(), **kwargs):
        super().__init__(**kwargs)
        self._loginUseCase = login_use_case

    def post(self, request):
        data = request.data

        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return self.bad_request("Email and password are required.")

        try:
            result = self._loginUseCase.execute(email, password)
            return self.json_response(result)
        except ValueError as e:
            return self.unauthorized(str(e))
