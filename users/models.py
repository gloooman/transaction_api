import binascii
import os

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


def generate_key():
    return binascii.hexlify(os.urandom(20)).decode()


class HMACKey(models.Model):
    key = models.CharField("Public Key", unique=True, max_length=40, default=generate_key)
    secret = models.CharField("Secret", max_length=40, default=generate_key)
    user = models.OneToOneField(User, related_name='hmac_key', on_delete=models.CASCADE, verbose_name="User")
    created = models.DateTimeField("Created", auto_now_add=True)

    class Meta:
        verbose_name = "HMACKey"
        verbose_name_plural = "HMACKey"

    def __str__(self):
        return f'{self.user} Public Key: {self.key}'
