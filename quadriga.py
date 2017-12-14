"""Wrapper for QuadrigaCX's API"""
from restclient import QuadrigaREST

class QuadrigaManager:

    def __init__(self, api_key, api_secret, client_id):
        self._client = QuadrigaREST(api_key, api_secret, client_id)

    def current_trading_info(self, book):
        response = self._client.get('/ticker?book=%s' % book)
        return response.json()

    def get_user_balance(self):
        response = self._client.post('/balance')
        return response.json()

    def get_dollar_amt(self, local_currency='cad'):
        currencies = ['btc', 'eth']

        # Get latest prices for each currency
        latest_info = {c:self.current_trading_info(c + '_' + local_currency) for c in currencies}
        prices = {c:float(latest_info[c]['last']) for c in ['eth', 'btc']}

        # Get current user balance
        my_balance = self.get_user_balance()
        my_balance = {c:float(my_balance[c + '_balance']) for c in ['eth', 'btc']}

        # Add up value of currencies in local currency
        print({c:prices[c] * my_balance[c] for c in currencies})
        value = [prices[c] * my_balance[c] for c in currencies]

        return sum(value)

    def get_user_transactions(self, offset=0, limit=50, sort='desc', book='btc_cad'):
        payload = {}
        payload['offset'] = offset
        payload['limit'] = limit
        payload['sort'] = sort
        payload['book'] = book

        response = self._client.post('/user_transactions', payload)
        return response.json()
