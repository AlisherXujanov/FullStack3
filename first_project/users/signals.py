import logging

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile

log = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    This function will be called every time a new user is created.
    It will create a new profile for the user.
    """
    # sender    == User
    # instance  == User object
    # created   == True or False
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
