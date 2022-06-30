import requests
import json

url = r"https://www.lazada.com.my/shop-mobiles/?bk-gadgets-store&from=wangpu&page=100&ajax=true"
x = requests.get(url)
json_obj = json.dumps(x.json())

with open("no.json", "w") as outfile:
    outfile.write(json_obj)