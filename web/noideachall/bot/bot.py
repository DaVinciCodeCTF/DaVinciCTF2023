from selenium import webdriver
import time
import os

HOST = 'web:5000'
URL = "http://"+ HOST + "/4d7wF98sgnu6LaSI9WI5"
BOT_COOKIE = 'dvCTF{1_H@v3_F0und_My_1d34!}'

opts = webdriver.ChromeOptions()
opts.add_argument("--headless")
opts.add_argument('--no-sandbox')
opts.add_argument('--disable-dev-shm-usage')
opts.add_argument('--disable-gpu')

chrome_prefs = {}
opts.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}

driver = webdriver.Chrome(options=opts)
driver.get(URL)
time.sleep(5)

while True:
    try:
        driver.add_cookie({'name': 'admin', 'value': BOT_COOKIE,})
        driver.get(URL)
    except Exception as e:
        print('Error checking page :', e)
    time.sleep(1)
