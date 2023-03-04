from selenium import webdriver
import time
import requests
from urllib.parse import urlparse, urlunparse
import re

HOST = "nginx"
URL = "http://" + HOST + "/"
LOGIN_URL = URL + "login/"
BOT_URL = URL + "e93717a75fefedbb76ecadf91a73b95e/"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "&zND4!96pA*dHR%9r86z"
netloc_regex = re.compile(r"(?:([^:]+)(?::(.*))?@)?([^:]+)(?::([\d]+))?")

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

login_page = requests.get(LOGIN_URL)
csrf_token = login_page.headers['Set-Cookie'].split('=')[1].split(';')[0]
csrf_middleware_token = re.findall(r'value="(.[^"]*)', login_page.text)[0]
data = {'csrfmiddlewaretoken': csrf_middleware_token, 'username': ADMIN_USERNAME, 'password': ADMIN_PASSWORD}
cookies = {'csrftoken': csrf_token}
BOT_COOKIE = requests.post(LOGIN_URL, data=data, cookies=cookies).request.headers['Cookie'].split('sessionid=')[1]

driver.add_cookie({'name': 'sessionid', 'value': BOT_COOKIE, 'httpOnly': True, 'path': '/'})

while True:
    try:
        res = requests.get(BOT_URL, cookies={'sessionid': BOT_COOKIE})
        if res.status_code == 200 and len(res.text) != 0:
            url = res.text

            scheme, netloc, path, params, query, fragment = urlparse(url)
            username, password, host, port = netloc_regex.search(netloc).groups()

            auth = ":".join(filter(None, (username, password)))
            address = ":".join(filter(None, (HOST, port)))
            netloc = "@".join(filter(None, (auth, address)))
            url = urlunparse((scheme, netloc, path, params, query, fragment))
            driver.get(url)
    except Exception as e:
        print('Error checking page :', e)
    time.sleep(10)
