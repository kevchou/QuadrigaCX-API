from quadriga import QuadrigaManager
from api_key import API_KEY, API_SECRET, CLIENT_ID

q = QuadrigaManager(API_KEY, API_SECRET, CLIENT_ID)
print(q.get_balance())
