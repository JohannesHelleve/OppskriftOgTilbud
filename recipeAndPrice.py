import json

from oppskrifterOpen import make_recipe
from OppskriftOgTilbud import push_to_mongo

recipe = make_recipe()


message = recipe['choices'][0]['message']['content']
print(message)
message['totPirce'] = 23
print(message)

"""try:
    with open("oppskirft.json", "w") as outfile:
        json.dump(recipe, outfile)
except:
    print(recipe[4][1][1])"""

"""f = open('oppskirft.json')

data = json.load(f)

print(data['choices'][0]['message']['content'])"""