from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np 
import requests

path = r"C:\Users\User\Desktop\priceshop\chromedriver_windows.exe"
# chrome_options = Options()
driver = webdriver.Chrome(path)
# wait = WebDriverWait(driver, 10)
# driver.get("https://www.lazada.com.my/products/honor-magicbook-x15-i3-2021-space-grey-8gb-ram-256gb-original-1-year-warranty-by-honor-malaysia-i2608649455-s11730638464.html?mp=1&freeshipping=1")
# time.sleep(10)

links = pd.read_csv("./Lazada Links.csv")
links_arr = list(links["Lazada Link"])

for link in links_arr:
	driver.get(link)
	# inner = driver.find_element(.get_attribute("innerHTML"))
	# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="module_product_title_1"]/div/div/h1')))
	driver.execute_script("window.stop();")
	# print(inner)
	time.sleep(3)

