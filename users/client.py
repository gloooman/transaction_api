import base64
import hashlib
import hmac
import json


class BaseHMAC:
    """
    Base class for HMAC Client cryptographic signing. Use
    this class if the programmer wants to implement thier
    own lookup for the HMAC `secret` cryptographic key
    """
    def __init__(self, user):
        """
        Args:
            user (User instance):
                that will be used to obtain the cryptographic key
        """
        self.secret = self.get_user_secret(user)

    @staticmethod
    def get_user_secret(user):
        """
        Retrieves the HMAC secret key to use for signing
        Note: can be overriden if the programmer wants to implement their
        own HMAC secret key retrieval based on the `User`
        """
        return user.hmac_key.secret

    def _calc_signature_from_str(self, s):
        byte_key = bytes.fromhex(self.secret)
        lhmac = hmac.new(byte_key, digestmod=hashlib.sha256)
        lhmac.update(s.encode('utf8'))
        return base64.b64encode(lhmac.digest())


class HMACAuthenticator(BaseHMAC):
    """
    Convince class for signing HMAC request Signatures
    using a `dict` instead of a `request`, which is what
    `HMACAuthenticator` relies on for calculating the HMAC
    Signatures
    """
    def calc_signature(self, headers, data=None):
        """
        Calculates the HMAC Signature based upon the headers and data
        """
        string_to_sign = self.string_to_sign(headers, data)
        return self._calc_signature_from_str(string_to_sign)

    @staticmethod
    def string_to_sign(headers, data=None):
        """
        Calculates the string to sign using the HMAC secret
        """
        s = '{method}-{path}-'.format(**headers)

        if data:
            s += json.dumps(data, separators=(',', ':'))
        return s
