from django.urls import path
from modules.users.infrastructure.controllers.findUserByIdController import (
    FindUserByIdController,
)

urlpatterns = [
    path("find/<str:id>/", FindUserByIdController.as_view(), name="find-user-by-id"),
]
