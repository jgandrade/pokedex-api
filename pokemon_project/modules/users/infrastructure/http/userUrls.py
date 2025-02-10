from django.urls import path
from modules.users.infrastructure.controllers.findUserByIdController import (
    FindUserByIdController,
)
from modules.users.infrastructure.controllers.loginController import (
    UserLoginController,
)
from modules.users.infrastructure.controllers.registerController import (
    UserRegisterController,
)

urlpatterns = [
    path("find/<str:id>/", FindUserByIdController.as_view(), name="find-user-by-id"),
    path("login/", UserLoginController.as_view(), name="user-login"),
    path("register/", UserRegisterController.as_view(), name="user-register"),
]
