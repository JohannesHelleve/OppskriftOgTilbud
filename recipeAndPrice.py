import json
from oppskrifterOpen import make_recipe
from OppskriftOgTilbud import push_to_mongo, get_grocery_data

#recipe = make_recipe()


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

print(data['choices'][0]['message']['content'])
print(type(data))
print(get_grocery_data())