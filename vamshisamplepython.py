import oauthlib
import pymysql
import oauthlib.oauth1
import requests
from oauthlib import oauth1

print("Vamsi")

host = '10.10.3.10'
user = 'technobahn'
password = 'willy007'
database = 'martjack'

"""db = pymysql.connect(host=host, user=user, passwd=password, database=database)

cursr = db.cursor()

cursr.execute('select * from tbllocation where locationid = 18340')

r = cursr.fetchall()"""


import requests
import oauthlib

Merchantid = 'f48fdd16-92db-4188-854d-1ecd9b62d066'
PublicKey = 'K5DYSCRC'
SecretKey = 'WHPT74UEQUYRZ33GUSBI7MGU'

LocationID = '18340'

url = 'http://www.testln.martjack.com/devapi/Location/Information/' + Merchantid + '/' + LocationID


import time




Client = oauthlib.oauth1.Client(client_key=PublicKey,client_secret=SecretKey, signature_method=oauthlib.oauth1.SIGNATURE_HMAC, signature_type=oauthlib.oauth1.SIGNATURE_TYPE_QUERY,timestamp= time.time())

uri, headers, body = Client.sign(url, http_method='GET')



response = requests.get(uri, headers = {'Accept': 'application/json'})


Locationrefcode = response.json()['Location']['LocationCode']



def SignatureMethod(url):
    Client = oauthlib.oauth1.Client(client_key=PublicKey,client_secret=SecretKey, signature_method=oauthlib.oauth1.SIGNATURE_HMAC, signature_type=oauthlib.oauth1.SIGNATURE_TYPE_QUERY,timestamp= time.time())
    uri, headers, body = Client.sign(url, http_method='GET')
    return uri

url2 = 'http://www.google.com'

print(SignatureMethod(url2))
    
print('vamsi')

