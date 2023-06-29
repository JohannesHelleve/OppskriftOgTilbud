import requests
import os
import json
from dotenv import load_dotenv
from pymongo import MongoClient
from bson import json_util
from ratelimit import limits
import argparse

load_dotenv()

BearerToken = os.getenv('BearerToken')
MongoAPI = os.getenv('MongoAPI')

headersKassal = {"Authorization": "Bearer " + BearerToken} 
client = MongoClient(MongoAPI)

db = client.Kassal



#@limits(calls=60, period=60)
def get_grocery_data(item):
    response = requests.get(f'https://kassal.app/api/v1/products/?search={item}&sort=price_asc&price_min=1', headers=headersKassal)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception('Error getting total items')

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Searches for the item in the Kassal API')
    parser.add_argument('item', type=str, help='Name of the item')

    args = parser.parse_args()
    get_grocery_data(args)


