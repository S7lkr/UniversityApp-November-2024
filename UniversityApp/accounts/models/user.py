from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from UniversityApp.accounts.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_staff = models.BooleanField(
        default=False
    )
    # primary credential
    USERNAME_FIELD = 'email'    # ALWAYS required (by default)
    REQUIRED_FIELDS = []        # no need to place 'email' field here
    objects = CustomUserManager()
