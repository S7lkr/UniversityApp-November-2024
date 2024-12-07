from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from UniversityApp.courses.choices_category import CourseChoices
from datetime import date
from django.utils.text import slugify


class Course(models.Model):
    _CATEGORY_MAX_LENGTH = 40
    _NAME_MAX_LENGTH = 70
    REQUIRED_MSG = "This field is required!"

    name = models.CharField(                # Python Web
        max_length=_NAME_MAX_LENGTH,
        unique=True,
        help_text=REQUIRED_MSG,
    )
    category = models.CharField(            # Web Design
        max_length=_CATEGORY_MAX_LENGTH,
        choices=CourseChoices.choices,
        help_text=f"Course category. {REQUIRED_MSG}"
    )
    slug = models.SlugField(
        null=True,
        blank=True,
        editable=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    start_date = models.DateField(
        default=date(2024, 11, 20),
        help_text=f"Course starting date. {REQUIRED_MSG}"
    )
    credits = models.PositiveSmallIntegerField(
        validators=(
            MinValueValidator(1),
            MaxValueValidator(50),
        ),
        help_text=REQUIRED_MSG,
    )
    duration = models.PositiveSmallIntegerField(
        help_text=REQUIRED_MSG,
        validators=(
            MinValueValidator(1),
            MaxValueValidator(24),
        ),
    )
    photo = models.URLField(
        null=True,
        blank=True,
        default="http://localhost:8000/static/img/course.jpg"
    )
    lector = models.CharField(
        max_length=40,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.category)      # Web Design -> web-design
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
