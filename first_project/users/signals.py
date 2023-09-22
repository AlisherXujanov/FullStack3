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
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """This function will be called every time a user is saved."""
    instance.profile.save()
    log.info(f"UserProfile has been created for {instance.username}")
