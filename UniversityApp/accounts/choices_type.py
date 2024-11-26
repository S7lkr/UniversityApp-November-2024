from django.db import models


class TypeChoices(models.TextChoices):
    LECTOR = "Lector", "Lector"
    STUDENT = "Student", "Student"
