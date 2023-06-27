import requests
import os
import json
from dotenv import load_dotenv
from pymongo import MongoClient
from bson import json_util
from ratelimit import limits

load_dotenv()

BearerToken = os.getenv('BearerToken')
MongoAPI = os.getenv('MongoAPI')

headersKassal = {"Authorization": "Bearer " + BearerToken} 
client = MongoClient(MongoAPI)

db = client.Kassal


response = requests.get('https://kassal.app/api/v1/products/', headers=headersKassal)

print(response)
#@limits(calls=60, period=60)
def get_grocery_data():
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception('Error getting total items')

#formating the data
def alter_data_bson(data):
    dataAltered = json.loads(json_util.dumps(data))
    return dataAltered

def push_to_mongo(dataAltered):
    db.Kassal.insert_one(dataAltered) 




