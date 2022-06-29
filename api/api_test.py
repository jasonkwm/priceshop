import requests
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# import datetime
# begin = datetime.datetime.now()
import time
prodKey = pd.read_csv("../selenium/Product Key.csv")
modelName = prodKey["PSmodelName"]

# prefs = {'profile.default_content_setting_values': {'images': 2,'plugins': 2, 'popups': 2, 'geolocation': 2, 
#         'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2, 
#         'mouselock': 2, 'mixed_script': 2, 'media_stream': 2, 
#         'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 
#         'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 
#         'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 
#         'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 
#         'durable_storage': 2}}
# chrome_options = Options()
# chrome_options.add_argument("--incognito")
# chrome_options.add_experimental_option("prefs", prefs)

# path = r"/Users/jakoh/Desktop/priceshop/chromedriver_87"
# service = Service(executable_path=path)
# driver = webdriver.Chrome(service=service, options=chrome_options)
# wait = WebDriverWait(driver, 3)

prodName = []
prodSeller = []
prodPrice = []
prodUrl = []
for name in modelName:
	url = f"https://www.lazada.com.my/catalog/?q={name}&ajax=true"
	x = requests.get(url)
	print(x.url)
	print(x.encoding)
	try:
		jsn = json.dumps(x)
	except:
		print("Unable to parse to json")
	time.sleep(2)
	# json_obj = x.json()
	# data = json_obj["mods"]["listItems"]
	# prodName.append(data["name"])
	# prodSeller.append(data["sellerName"])
	# prodPrice.append(data["price"])
	# prodUrl.append(data["itemUrl"])

df = pd.DataFrame({
	"Product Url" : prodUrl,
	"Product Name" : prodName,
	"Seller Name": prodSeller,
	"Product Price": prodPrice,
})
ile_name = 'ajax.csv'
df.to_csv(f'~/Desktop/priceshop/{file_name}')
print(f"Output to: {file_name}")
# print(datetime.datetime.now() - begin)
# with open("test.json", "w") as outfile:
#     outfile.write(json_obj)