import hmac

from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from .client import HMACAuthenticator

User = get_user_model()


class HMACAuthentication(BaseAuthentication):

    def authenticate(self, request):
        data = {}
        if request.method == 'GET':
            data = request.GET
        if request.method == 'POST':
            data = request.data

        signature = self.get_signature(data)
        user = self.get_user(data)

        headers = {
            'method': request.method,
            'path': request.META['PATH_INFO'],
        }

        b64 = HMACAuthenticator(user).calc_signature(headers, data)
        if not hmac.compare_digest(b64, signature):
            raise AuthenticationFailed()

        return user, None

    @staticmethod
    def get_user(data):
        try:
            public_key = data.pop('public_key')
            return User.objects.get(hmac_key__key=public_key)
        except (KeyError, User.DoesNotExist):
            raise AuthenticationFailed()

    @staticmethod
    def get_signature(data):
        try:
            signature = data.pop('sign')
        except KeyError:
            raise AuthenticationFailed()
        return signature.encode(encoding='UTF-8')
