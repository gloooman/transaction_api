from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import HMACKey

User = get_user_model()


@receiver(post_save, sender=User)
def create_hmac_key(sender, instance=None, created=False, **kwargs):
    if created:
        HMACKey.objects.create(user=instance)
