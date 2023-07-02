import requests
import os
import json
from dotenv import load_dotenv
from pymongo import MongoClient
from bson import json_util
from ratelimit import limits
import sys

load_dotenv()

BearerToken = os.getenv('BearerToken')
MongoAPI = os.getenv('MongoAPI')

headersKassal = {"Authorization": "Bearer " + BearerToken} 
client = MongoClient(MongoAPI)

db = client.Kassal



#@limits(calls=60, period=60)
def get_grocery_data(item):
    response = requests.get(f'https://kassal.app/api/v1/products/?search={item}&sort=price_asc&price_min=1&size=5', headers=headersKassal)
    if response.status_code == 200:
        data = response.json()
        prettyData = data_to_pretty_list(data)
        return prettyData
    else:
        raise Exception('Error getting total items')

def data_to_pretty_list(data):
    i = 0
    prettyList = []
    while i < len(data['data']):
        prettyList.append([data['data'][i]['name'], data['data'][i]['price_history'][0]['price'], data['data'][i]['store']['name'] ])
        i += 1
    return prettyList
"""groceryData = get_grocery_data()
print(type(groceryData))
i = 0

while i < len(groceryData['data']):
   print(f"{groceryData['data'][i]['name']} koster {groceryData['data'][i]['price_history'][0]['price']} kr idag {groceryData['data'][i]['store']['name']}")
   i += 1"""


#formating the data
def alter_data_bson(data):
    dataAltered = json.loads(json_util.dumps(data))
    return dataAltered

def push_to_mongo(dataAltered):
    db.Kassal.insert_one(dataAltered) 




