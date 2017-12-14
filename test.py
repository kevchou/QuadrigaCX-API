from quadriga import QuadrigaManager
from api_key import API_KEY, API_SECRET, CLIENT_ID

q = QuadrigaManager(API_KEY, API_SECRET, CLIENT_ID)
print(q.get_user_balance())



print(q.get_dollar_amt('cad'))
