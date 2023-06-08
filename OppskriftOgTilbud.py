import requests
import config
import json
from pymongo import MongoClient
from bson import json_util
from ratelimit import limits

headersKassal = {"Authorization": "Bearer " + config.BearerToken}
client = MongoClient(config.UserMongo)

db = client.Kassal


response = requests.get('https://kassal.app/api/v1/products/', headers=headersKassal)

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

def push_grocery_to_mongo(dataAltered):
    db.Kassal.insert_one(dataAltered) 




