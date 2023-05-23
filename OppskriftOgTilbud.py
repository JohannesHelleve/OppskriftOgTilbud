import requests
import config


API_KEY = config.api_key

# Make the request to the Tjek API
response = requests.get("https://api.tjek.no/v1/products", headers={"Authorization": "Bearer " + API_KEY})

if response.status_code == 200:
    # Get the products from the response
    products = response.json()["products"]

    # Filter the products by store and sale
    products = [product for product in products if product["brand"] == "Bunnpris" and product["sale"] == True]

    # Print the list of products
    for product in products:
        print(product["name"] + " is on sale for " + product["price"])

else:
    print("Error: " + response.status_code)