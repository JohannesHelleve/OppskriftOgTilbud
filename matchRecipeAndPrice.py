import json
from oppskrifterOpen import make_recipe, get_ingredients,get_weight_ingrdient
from OppskriftOgTilbud import push_to_mongo, get_grocery_data, data_to_pretty_list

recipe = make_recipe()

ingredients = get_ingredients(recipe)
print(ingredients)

totalSum = 0
for ingredient in ingredients:
    print(ingredient[2])

    billigsteVarer = get_grocery_data(ingredient[2])
    totalSum += billigsteVarer[0][1]

print(recipe['choices'][0]['message']['content'])
print(f"Denne middag koster {totalSum}kr")

def add_price_to_dict(dict, price):
    dict['totPrice'] = price




