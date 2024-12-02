from django.db import models
from UniversityApp.accounts.models import Profile
from UniversityApp.courses.models import Course


class Comment(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['created_at'])
        ]
        ordering = ['-created_at']    # DESC

    content = models.TextField(
        max_length=200,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    user = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
    )
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
    )
