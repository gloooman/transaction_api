from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from transactions.models import Tag, Transaction


class CreatableSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get(**{self.slug_field: data})
        except ObjectDoesNotExist:
            return self.get_queryset().create(**{self.slug_field: data})  # to create the object
        except (TypeError, ValueError):
            self.fail('invalid')


class TransactionSerializer(serializers.ModelSerializer):
    tags = CreatableSlugRelatedField(many=True, slug_field='name', queryset=Tag.objects.all())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    transaction_data = serializers.JSONField()

    class Meta:
        model = Transaction
        exclude = ['id']
