

import requests

selldata  = { 'sell':  { 
		'location_data': [ 'X', 'Y'],
		'well_data': [ 'API', 'etc'], 
		'royalty_data': [ 'pay1', 'pay2', ],
		}
}


SERVER = 'http://127.0.0.1:8000/'


headers = {'X-CSRFToken': csrf_token_value, 'Referer': URL}

r = requests.post("http://127.0.0.1:8000/getMWdata/", data=selldata, headers=headers);
print(r)