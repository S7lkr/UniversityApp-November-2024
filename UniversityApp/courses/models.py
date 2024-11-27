from datetime import date
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
        help_text="This field is required!"
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
        null=True,
        blank=True,
    )
    credits = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )
    duration = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
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

    def save(self, *args, **kwargs):    # override save method
        super().save(*args, **kwargs)   # get all functionalities from parent's "save()" method
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")  # HTML, CSS & JS --> html-css-js
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
