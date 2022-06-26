import requests
import json

url = r"https://www.lazada.com.my/mycom/?ajax=true&from=wangpu&langFlag=en&page=1&pageTypeId=2&q=All-Products"
x = requests.get(url)
json_obj = json.dumps(x.json())

with open("demo.json", "w") as outfile:
    outfile.write(json_obj)