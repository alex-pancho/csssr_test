import requests
import json
'''
Swagger API call v 0.5
'''

base_url = 'https://superhero.qa-test.csssr.com'

# get
def get_superheroes(hid=None, api_link="superheroes"):
    api_url = f"{base_url}/{api_link}" if hid is None else f"{base_url}/{api_link}/{hid}"
    r = requests.get(api_url)
    return r
# post
def post_superheroes(dto):
    api_url = f"{base_url}/superheroes"
    api_data = dto
    r = requests.post(api_url, json=api_data)
    return r    
# put
def put_superheroes(hid, dto):
    api_url = f"{base_url}/superheroes/{hid}"
    api_data = dto
    r = requests.put(api_url, json=api_data)
    return r  

# delete
def del_superheroes(hid):
    api_url = f"{base_url}/superheroes/{hid}"
    r = requests.delete(api_url)
    return r

# print request info
def req_info(r):
    status_code = r.status_code
    try:
        r_body = r.json()
    except json.decoder.JSONDecodeError:
        r_body = r.content
    return status_code, r_body

def print_me(r):
    status_code = r[0]
    r_body = r[1]
    print("Status Code:", status_code)
    print("We get:", r_body)

if __name__ == '__main__':
    # small tests
    
    hd = {"id": 1,
      "fullName": "Skitter",
      "birthDate": "1985-06-23",
      "city": "Brokton Bay",
      "mainSkill": "Bug control",
      "gender": "f",
      "phone": "+17569009999"
    }
    
    r = get_superheroes()
    print_me(req_info(r))
    r = post_superheroes(hd)
    print(r.request.body)
    print_me(req_info(r))
