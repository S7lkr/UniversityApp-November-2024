from datetime import date

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify
from UniversityApp.courses.choices_category import CourseChoices


class Course(models.Model):
    CATEGORY_MAX_LENGTH = 40
    NAME_MAX_LENGTH = 70

    name = models.CharField(                # Python Web
        max_length=NAME_MAX_LENGTH,
        unique=True,
        help_text="This field is required!"
    )
    category = models.CharField(            # Web Design
        max_length=CATEGORY_MAX_LENGTH,
        choices=CourseChoices.choices,
        help_text="Course category: This field is required!"
    )
    slug = models.SlugField(
        null=True,
        blank=True,
        editable=False,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    start_date = models.DateField(
        default=date.today(),
        help_text="Course starting date: This field is required!"
    )
    credits = models.PositiveSmallIntegerField(
        help_text="Required field!",
        validators=(
            MinValueValidator(1),
        ),
    )
    duration = models.PositiveSmallIntegerField(
        help_text="Required field!",
        validators=(
            MinValueValidator(1),
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
