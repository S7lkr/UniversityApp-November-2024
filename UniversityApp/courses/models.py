from django.db import models
from django.utils.text import slugify
from UniversityApp.courses.course_categories import CourseChoices


class Course(models.Model):
    CATEGORY_MAX_LENGTH = 40
    NAME_MAX_LENGTH = 70

    name = models.CharField(                # Python Web
        max_length=NAME_MAX_LENGTH,
    )
    category = models.CharField(            # Web Design
        max_length=CATEGORY_MAX_LENGTH,
        choices=CourseChoices.choices,
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        editable=False,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    credits = models.PositiveSmallIntegerField(
        default=0,
    )
    photo = models.URLField(
        null=True,
        blank=True,
        default="http://localhost:8000/static/img/course.jpg"
    )

    def save(self, *args, **kwargs):    # override save method
        super().save(*args, **kwargs)   # get all functionalities from parent's "save()" method
        if not self.slug:
            self.slug = slugify(self.category)  # Web Design -> web-design
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
