from django.db import models
from UniversityApp.Courses.course_categories import CourseChoices


class Course(models.Model):
    CATEGORY_MAX_LENGTH = 40
    NAME_MAX_LENGTH = 70

    name = models.CharField(                # Python Web
        max_length=NAME_MAX_LENGTH,
    )
    category = models.CharField(            # Web Design
        max_length=CATEGORY_MAX_LENGTH,
        choices=CourseChoices.choices,
        default=CourseChoices.OTHER,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    credits = models.PositiveSmallIntegerField(
        default=0,
        null=True,
        blank=True,
    )
    photo = models.URLField(
        default="http://localhost:8000/static/img/course.jpg"
    )
