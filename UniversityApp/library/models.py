from django.db import models
from django.core.validators import MinLengthValidator
from UniversityApp.accounts.models import CustomUser
from datetime import date


# "Book" Abstract class
class Literature(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
        ],
        help_text="Title must be at least 2 characters long or more."
    )
    content = models.TextField(
        max_length=1000,
    )
    publish_date = models.DateField()
    pages = models.PositiveSmallIntegerField(
        default=180,
    )

    def __str__(self):
        return f"{self.title} from {self.publish_date}"


class Book(Literature):
    author = models.ForeignKey(
        to=CustomUser,
        on_delete=models.SET,
        related_name='books',
    )
    image = models.URLField(
        default='http://localhost:8000/static/img/book.jpg',
    )


class SoftwareJournal(Literature):
    image = models.URLField(
        default='http://localhost:8000/static/img/journal2.jpg',
    )
