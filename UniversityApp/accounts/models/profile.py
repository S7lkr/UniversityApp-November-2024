from django.db import models
from django.contrib.auth import get_user_model
from UniversityApp.courses.models import Course
from django.core.validators import MinLengthValidator
from UniversityApp.validators import AlphabeticValidator

UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            AlphabeticValidator(),
        ],
        help_text="This field is required!"
    )
    last_name = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(2),
            AlphabeticValidator(),
        ],
        null=True,
        blank=True,
    )
    personal_image = models.URLField(
        null=True,
        blank=True,
    )
    age = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )
    bio = models.TextField(
        null=True,
        blank=True,
    )
    is_lector = models.BooleanField(
        default=False,
    )
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
    )
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        null=True,
        blank=True,                 # Profile.course_id -> person's course
        related_name='profiles',    # Course2.profiles -> course's all people
    )

    def __str__(self):
        if self.last_name:
            return self.first_name + " " + self.last_name
        return self.first_name
