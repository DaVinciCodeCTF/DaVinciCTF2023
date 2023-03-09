import json
import base64

fh = open('Local State', 'rb')
encrypted_key = json.load(fh)

encrypted_key = encrypted_key['os_crypt']['encrypted_key']

decrypted_key = base64.b64decode(encrypted_key)

open("dec_data",'wb').write(decrypted_key[5:])
