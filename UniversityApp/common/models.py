from django.db import models
from django.contrib.auth import get_user_model
from UniversityApp.courses.models import Course

User = get_user_model()


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
        to=User,
        on_delete=models.CASCADE,
    )
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
    )
