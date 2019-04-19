

import requests, json
from secret import SECRET_KEY

selldata  = { 'sell':  { 
		'location_data': [ 'X', 'Y'],
		'well_data': [ 'API', 'etc'], 
		'royalty_data': [ 'pay1', 'pay2', ],
		}
}

payload = { 'mdata': selldata	,  	}
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'x-csrf-token': SECRET_KEY}
r = requests.post("http://127.0.0.1:8000/getMWdata/", json=payload, headers	= headers)


print(r)