import  json
import  numpy as np
import  pandas as pd

with open("demo.json") as json_file:
    data = json.load(json_file)

for items in data["mods"]["listItems"]:
    print("Name: " +items["name"])
    print("Seller Name: " +  items["sellerName"])
    print("Price: " + items["price"])
    print("Url: "+ items["itemUrl"] + "\n")
# print(data["mods"]["listItems"][0])