from pokemon_project.core.domain.models.baseModel import BaseModel
from django.db import models
from django.utils import timezone


class User(BaseModel):
    user_id = models.CharField(max_length=36, unique=True, primary_key=True)
    full_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    profile_picture_url = models.URLField(blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    pokemon_store_id = models.CharField(max_length=36, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
