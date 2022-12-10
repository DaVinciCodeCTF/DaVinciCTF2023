from selenium import webdriver
import time
import os

HOST = os.environ['HOST']
URL = "http://"+ HOST + ":5000/list_files?"
BOT_COOKIE = 'iV414B%*@RqqyiptLE$p'

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
driver.add_cookie({'name': 'admin', 'value': BOT_COOKIE, 'httpOnly': True, 'path': '/'})

while True:
    try:
        driver.add_cookie({'name': 'admin', 'value': BOT_COOKIE,})
        driver.get(URL)
    except Exception as e:
        print('Error checking page :', e)
    time.sleep(10)