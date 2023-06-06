import requests
import config
import json
from pymongo import MongoClient

headersKassal = {"Authorization": "Bearer " + config.BearerToken}
headersMongo = {}

test3 = [{'name': 'Audi', 'price': 52642},
    {'name': 'Mercedes', 'price': 57127},
    {'name': 'Skoda', 'price': 9000},
    {'name': 'Volvo', 'price': 29000},
    {'name': 'Bentley', 'price': 350000},
    {'name': 'Citroen', 'price': 21000},
    {'name': 'Hummer', 'price': 41400},
    {'name': 'Volkswagen', 'price': 21600}
    ]
client = MongoClient(config.UserMongo)

db = client.Kassal

db.Test.insert_many(test3)

response = requests.get('https://kassal.app/api/v1/products', headers=headersKassal)
print(response)

db.Kassal.insert_one(response)

