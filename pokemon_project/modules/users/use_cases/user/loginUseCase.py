from core.domain.useCase import UseCase
from modules.users.persistence.userRepository import UserRepository
from modules.users.domain.services.passwordService import PasswordService
from modules.users.domain.services.jwtService import JWTService


class UserLoginUseCase(UseCase):
    def __init__(
        self,
        user_repository=UserRepository(),
        password_service=PasswordService(),
        jwt_service=JWTService(),
    ):
        self._userRepository = user_repository
        self._passwordService = password_service
        self._jwtService = jwt_service

    def execute(self, email: str, password: str) -> dict:
        user = self._userRepository.findByEmail(email)
        if not user:
            raise ValueError("Invalid email.")

        is_valid_password = self._passwordService.validate_password(
            password, user.password
        )
        if not is_valid_password:
            raise ValueError("Invalid password.")

        token = self._jwtService.create_access_token(
            {
                "id": user.id,
                "userId": user.userId,
                "fullName": user.fullName,
                "userName": user.userName,
                "email": user.email,
            }
        )

        return {
            "message": "Login successful.",
            "token": token,
            "user": {
                "id": user.id,
                "userId": user.userId,
                "fullName": user.fullName,
                "userName": user.userName,
                "email": user.email,
            },
        }
