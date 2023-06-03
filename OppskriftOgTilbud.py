import requests
import config
import _json

endpoint = 'https://kassal.app/api/v1/'
headers = {"Authorization": "Bearer " + config.BearerToken}

response = requests.get('https://kassal.app/api/v1/products', headers=headers)
print(response)
print(response.json())