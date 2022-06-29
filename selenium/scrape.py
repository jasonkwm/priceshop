from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
import requests
import datetime
begin = datetime.datetime.now()

prefs = {'profile.default_content_setting_values': {'images': 2,'plugins': 2, 'popups': 2, 'geolocation': 2, 
        'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2, 
        'mouselock': 2, 'mixed_script': 2, 'media_stream': 2, 
        'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 
        'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 
        'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 
        'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 
        'durable_storage': 2}}
chrome_options = Options()
chrome_options.add_argument("--incognito")
# chrome_options.add_argument('--headless')
chrome_options.add_experimental_option("prefs", prefs)

path = r"/Users/jakoh/Desktop/priceshop/chromedriver_87"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=chrome_options)

links = pd.read_csv("~/Desktop/priceshop/selenium/Lazada Links.csv")
links.drop(columns=['Unnamed: 1', 'Notes for cadets'], inplace=True)


def ft_find_elem(link, model):
	prodUrl = link
	prodName = driver.find_element(By.XPATH, '//*[@id="module_product_title_1"]/div/div/h1').text
	prodPrice = driver.find_element(By.XPATH, '//*[@id="module_product_price_1"]/div/div/span').text
	prodQty = driver.find_element(By.XPATH, '//*[@id="module_quantity-input"]/div/div/span').text
	prodModel = model
	return [prodUrl, prodName, prodModel, prodQty, prodPrice]


prodUrl = []
prodName = []
prodPrice = []
prodQty = []
prodModel = []

def ft_append(arr):
	prodUrl.append(arr[0])
	prodName.append(arr[1])
	prodModel.append(arr[2])
	prodQty.append(arr[3])
	prodPrice.append(arr[4])

for link in links["Lazada Link"]:
	word = 0
	driver.get(link)
	arr = ft_find_elem(link, "")
	try:
		h6 = driver.find_elements(By.XPATH, '//*[@id="module_sku-select"]/div/div/div/h6')
		i = 0
		for h in h6:
			i += 1
			lower = h.text.lower()
			if "storage" in lower or "spec" in lower:
				word = 1
				txt = driver.find_elements(By.XPATH, f'//*[@id="module_sku-select"]/div/div[{i}]/div/div/div[2]/span')
				for t in txt:
					t.click()
					arr = ft_find_elem(link, t.text)
					ft_append(arr)
					time.sleep(1)
				break
	except:
		print("Error in try case.")
	if word == 0:
		ft_append(arr)
	time.sleep(2)
driver.quit()
df = pd.DataFrame({
	"productURL" : prodUrl,
	"productName from URL" : prodName,
	"Variant from URL": prodModel,
	"Stock Status from URL": prodQty,
	"price": prodPrice
})

file_name = 'temp.csv'
df.to_csv(f'~/Desktop/priceshop/{file_name}')
print(f"Output to: {file_name}")
with open("time.txt", "w") as outfile:
    outfile.write(str(datetime.datetime.now() - begin))
