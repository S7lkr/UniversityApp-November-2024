from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from UniversityApp.validators import LettersOnlyValidator

UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            LettersOnlyValidator(),
        ]
    )
    last_name = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(2),
            LettersOnlyValidator(),
        ],

    )
    age = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )
    personal_image = models.URLField(
        null=True,
        blank=True,
    )
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.first_name + " " + self.last_name
