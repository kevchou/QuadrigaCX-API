"""Quadriga API"""
import hmac
import hashlib
import time
import requests


class QuadrigaREST:
    """Client that uses Quadriga API"""

    API_URL = 'https://api.quadrigacx.com/v2'

    def __init__(self, api_key, api_secret, client_id):
        self._api_key = api_key
        self._hmac_key = api_secret.encode('utf-8')
        self._client_id = client_id

    def _signature(self, nonce):
        msg = str(nonce) + self._client_id + self._api_key
        return hmac.new(
            key=self._hmac_key,
            msg=msg.encode('utf-8'),
            digestmod=hashlib.sha256
        ).hexdigest()

    def get(self, url, params=None):
        """GET request"""
        response = requests.get(
            url=self.API_URL + url,
            params=params)

        return response

    def post(self, url, payload=None):
        """POST request"""
        nonce = int(time.time() * 1000)
        signature = self._signature(nonce)

        if payload is None:
            payload = {}

        payload['key'] = self._api_key
        payload['nonce'] = nonce
        payload['signature'] = signature

        response = requests.post(
            url=self.API_URL + url,
            json=payload
        )

        return response
