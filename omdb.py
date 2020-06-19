import requests
import json
'''
Swagger API call v 0.5
'''

base_url = 'http://www.omdbapi.com'

apikey = '86487c4f'

# get ?apikey=[yourkey]
def get_omdb(id_or_name, param="t"):
    if param == "i":
        ask = "i"
    else:
        ask = "t"
    upload = {ask: id_or_name, 'apikey': apikey}
    r = requests.get(base_url, params=upload)
    return r

r = get_omdb("Shrek")
print(r.content)
r = get_omdb("tt3896198", "i")
print(r.content)