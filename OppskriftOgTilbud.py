import requests
import config
import json
from pymongo import MongoClient

headersKassal = {"Authorization": "Bearer " + config.BearerToken}
headersMongo = {}

client = MongoClient()
db = client['test']
response = requests.get('https://kassal.app/api/v1/products', headers=headersKassal)


#print(response.json())