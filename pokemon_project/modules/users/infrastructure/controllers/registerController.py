from rest_framework.response import Response
from rest_framework import status
from core.infrastructure.baseController import BaseController
from modules.users.use_cases.user.registerUseCase import UserRegisterUseCase


class UserRegisterController(BaseController):

    def __init__(self, register_use_case=UserRegisterUseCase(), **kwargs):
        super().__init__(**kwargs)
        self._registerUseCase = register_use_case

    def post(self, request):
        try:
            user_data = request.data
            result = self._registerUseCase.execute(
                user_name=user_data.get("user_name", ""),
                full_name=user_data.get("full_name", ""),
                email=user_data.get("email", ""),
                password=user_data.get("password", ""),
            )
            return Response(result, status=status.HTTP_201_CREATED)

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_409_CONFLICT)

        except Exception as e:
            return Response(
                {"error": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
