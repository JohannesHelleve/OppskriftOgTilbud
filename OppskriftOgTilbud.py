import requests
import config
import json

endpoint = 'https://kassal.app/api/v1/'
headers = {"Authorization": "Bearer " + config.BearerToken}

response = requests.get('https://kassal.app/api/v1/products', headers=headers)

response_data = json.loads(response.json)

response_formated = json.dumps(response_data, indent = 2 )

print(response_formated)