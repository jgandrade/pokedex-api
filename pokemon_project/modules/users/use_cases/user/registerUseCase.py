from core.domain.useCase import UseCase
from modules.users.persistence.userRepository import UserRepository
from modules.users.domain.services.passwordService import PasswordService
from modules.users.domain.services.emailService import EmailService
from modules.users.domain.services.jwtService import JWTService
from modules.users.domain.user import User


class UserRegisterUseCase(UseCase):

    def __init__(
        self,
        user_repository=UserRepository(),
        password_service=PasswordService(),
        email_service=EmailService(),
        jwt_service=JWTService(),
    ):
        self.userRepository = user_repository
        self.password_service = password_service
        self.email_service = email_service
        self.jwt_service = jwt_service

    def execute(
        self,
        user_name: str = "",
        full_name: str = "",
        email: str = "",
        password: str = "",
    ) -> dict:
        existing_user_email = self.userRepository.findByEmail(email)
        if existing_user_email:
            raise ValueError("User with this email already exists.")

        existing_user_name = self.userRepository.findByEmail(user_name)
        if existing_user_name:
            raise ValueError("User with this username already exists.")

        hashed_password = self.password_service.encrypt_password(password)

        user = User.createWithDefaults(
            {
                "fullName": full_name,
                "userName": user_name,
                "email": email,
                "password": hashed_password,
            }
        )

        self.userRepository.save(user)

        token = self.jwt_service.create_email_token(
            {
                "id": user.id,
                "userId": user.userId,
                "fullName": user.fullName,
                "userName": user.userName,
                "email": email,
            }
        )

        # self.email_service.send_email_verification(email, full_name, token)

        return {
            "id": user.id,
            "userId": user.userId,
            "fullName": user.fullName,
            "userName": user.userName,
            "email": email,
        }
