from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from UniversityApp import settings
from UniversityApp.accounts.models import Profile

User = get_user_model()


# Django signal -> on USER creation, automatically creates PROFILE
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def make_profile(sender, instance: User, created: bool, **kwargs):
    if created:                     # when User model created
        print(instance.email)
        Profile.objects.create(     # a Profile model will be created too
            first_name='',
            last_name=None,       # initial Profile data
            age=None,
            personal_image="http://127.0.0.1:8000/static/img/team.jpg",
            user=instance,
        )
