import json
from oppskrifterOpen import make_recipe
from OppskriftOgTilbud import push_to_mongo, get_grocery_data

"""recipe = make_recipe()"""


"""
message = recipe['choices'][0]['message']['content']
messageDict = json.loads(message)
print(type(messageDict))
messageDict['totPirce'] = 23
print(messageDict)"""

"""try:
    with open("oppskirft.json", "w") as outfile:
        json.dump(recipe, outfile)
except:
    print(recipe[4][1][1])"""

f = open('oppskirft.json')

data = json.load(f)

message2 = data['choices'][0]['message']['content']
dataDict = json.loads(message2)
print(message2)
print(type(dataDict))

def match_price_to_item(recipeJson):
    i = 0
    recipeItemsLen = len(recipeJson['ingredients'])
    while i < recipeItemsLen:
        print(f'{recipeJson["ingredients"][i]["amount"]} {recipeJson["ingredients"][i]["unit"]} {recipeJson["ingredients"][i]["keyword"]}')
        i += 1
        if i == recipeItemsLen :
            break

match_price_to_item(dataDict)