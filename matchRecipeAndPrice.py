import json
from oppskrifterOpen import make_recipe
from OppskriftOgTilbud import push_to_mongo, get_grocery_data

#recipe = make_recipe()


def add_price_to_dict(dict, price):
    dict['totPrice'] = price

def make_string_dict(message):
    string = message['choices'][0]['message']['content']
    stringAsDict = json.loads(string)
    return stringAsDict


f = open('oppskirft.json')

data = json.load(f)

message2 = data['choices'][0]['message']['content']
dataDict = json.loads(message2)
print(message2)
print(type(dataDict))

def get_ingredients(recipeJson):
    ingredients = []
    i = 0
    recipeItemsLen = len(recipeJson['ingredients'])
    while i < recipeItemsLen:
        ingredient = {recipeJson["ingredients"][i]["amount"], recipeJson["ingredients"][i]["unit"], recipeJson["ingredients"][i]["keyword"]}
        ingredients.append(ingredient)
        i += 1
        if i == recipeItemsLen :
            break
    return ingredients

print(get_ingredients(dataDict))
print(get_grocery_data(23))
#match_price_to_item(make_string_dict(recipe))