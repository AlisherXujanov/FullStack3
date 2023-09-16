import logging

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile

log = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if (created and not kwargs.get('raw')):
        Profile.objects.create(user=instance)
        log.info(f"UserProfile has been created for {instance.username}")
