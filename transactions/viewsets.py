from rest_framework.permissions import AllowAny
from rest_framework import viewsets


from transactions.models import Transaction
from users.authentication import HMACAuthentication
from . import serializers


class TransactionViewSet(viewsets.ModelViewSet):
    """
    Provides basic CRUD functions for the Transaction model
    """
    lookup_field = 'uid'
    authentication_classes = (HMACAuthentication, )
    queryset = Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get', 'post']

    def get_authenticators(self):
        if self.request.method == 'POST':
            return super().get_authenticators()
        return []
