import json
import requests
import os

api_token = "token " + os.getenv('SQUAC_API_TOKEN')
print(api_token)
api_base = os.getenv('SQUAC_API_BASE')

headers = {'Content-Type': 'application/json',
           'Authorization': api_token }

print(headers)
def get_account():

    api_url = api_base + "user/me"

    response = requests.get(api_url, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


account = get_account()
print(account)
if account is not None:
    print("Here's your info: ")
    for k,v in account.items():
        print(k)

else:
    print('[!] Request Failed')
