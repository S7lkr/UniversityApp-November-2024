from django.db import models
from django.core.validators import MinLengthValidator
from UniversityApp.accounts.models import CustomUser


# "Book" Abstract class
class Literature(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
        ]
    )
    content = models.TextField(
        max_length=1000,
    )
    image = models.URLField(
        default=None,
    )
    publish_date = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.title} from {self.publish_date}"


class Book(Literature):
    author = models.ForeignKey(
        to=CustomUser,
        on_delete=models.SET,
        related_name='books',
    )
    pages = models.PositiveSmallIntegerField()


class Journal(Literature):
    pass
