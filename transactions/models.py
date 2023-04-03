import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tag(models.Model):
    name = models.CharField('Тag Name', max_length=64, unique=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    uid = models.CharField(max_length=64, default=uuid.uuid4, unique=True)
    device_timestamp = models.DateTimeField(auto_now_add=False)
    received_at = models.DateTimeField(auto_now_add=False)
    tags = models.ManyToManyField(Tag)
    transaction_data = models.TextField()

    def __str__(self):
        return self.uid
