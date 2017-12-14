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

    def get_user_transactions(self, offset=0, limit=50, sort='desc', book='btc_cad'):

        payload = {}
        payload['offset'] = offset
        payload['limit'] = limit
        payload['sort'] = sort
        payload['book'] = book

        response = self._client.post('/user_transactions', payload)
        return response.json()
