from django.db import models
from django.core.validators import MinLengthValidator
from UniversityApp.validators import AlphabeticValidator


class Lesson(models.Model):
    _REQUIRED = "This field is required."
    title = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
        ],
        help_text=_REQUIRED,
    )
    description = models.TextField(
        max_length=400,
        null=True,
        blank=True,
    )
    readme = models.CharField(
        max_length=150,
        help_text="Enter lesson's main points, separated with semicolon ';'",
    )
    course = models.ForeignKey(
        to='courses.Course',
        on_delete=models.CASCADE,
        related_name='lessons',
    )
