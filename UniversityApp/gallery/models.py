from django.db import models


class Album(models.Model):
    title = models.CharField(
        max_length=100,
    )
    cover = models.ImageField(
        upload_to='',
    )
    created_at = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.title


class Photo(models.Model):
    photo = models.ImageField(
        upload_to='',
    )
    album = models.ForeignKey(
        to=Album,
        on_delete=models.CASCADE,
        related_name='photos',
    )
