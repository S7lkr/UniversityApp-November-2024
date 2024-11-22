from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from UniversityApp.accounts.managers import CustomUserManager
from UniversityApp.validators import PasswordValidator


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'This email is already taken. Please enter a different one!',
        },
    )
    password = models.CharField(
        max_length=16,
        validators=[
            MinLengthValidator(4),
            PasswordValidator(),
        ]
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_staff = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'email'    # first credential used in auth, required by default
    REQUIRED_FIELDS = []        # so not necessary to place it in REQUIRED_FIELDS
    objects = CustomUserManager()
