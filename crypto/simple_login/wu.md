# Writeup

## Challenge 
The challenge consists of a simple web application allowing the user to create users and to log in. The problem is, a hash is asked in order to log in but we can't find any information about a hash on the website.

---
## Solution
First, after some digging we find a **login.php.bak** present on the server (<host>:<port>/login.php.bak). 

In this file there are several important informatios that can be exploited. The first one being the format of the hash we need to provide : 
```php
if (md5($my_salt . $username) === $hash)
```
Hence, we need to create a hash of our username using a salt.
Unfortunately, we don't have the salt but we have some informations about it :
```php
assert(strlen($my_salt) == 27);
assert(md5($my_salt) == "46eaafcb93f2c5f8fc215cac38e1eaaf");
```
We know its length and its md5sum. 

With this information, we can perform a hash length extension attack. I won't get into details of why it is vulnerable, but here is [a good article](https://deeprnd.medium.com/length-extension-attack-bff5b1ad2f70) if you want to understand this attack. Note that not only md5 but all algorithms using 	Merkle–Damgård construction are vulnerable (sha1 is another example).

The best tool to perform such an attack is **HashPump**.

We can simply clone the [github repo](https://github.com/bwall/HashPump) and try to use it. However, we'll quickly face a problem. 

Usually, hash length extensions attacks are performed on hash that are composed of the salt or the secret already appended to data. This means that we have `md5(secret+data)` and we want to have `md5(secret+my_data)`.

With HashPump this is done with this command : 
```
hashpump -s md5(secret+data) -d data -a my_data -k 27

-s : original signature
-d : original data
-a : data to append
-k : size of the secret
```
However in this challenge, we only have `md5(secret)`. The attack still works but HashPump won't let us put an empty string in the `-d` argument. HashPump will keep giving us a prompt to input original data.

To solve this problem, we can clone the HashPump repository and make slight modifications before `make`.

In `main.cpp`, remove the whole `if` statement line 255:
```cpp
if(data.size() == 0)
	{
		cout << "Input Data: ";
		cin >> data;
	}
```
In `hashpumpy.cpp`, remvoe the whole `if` statement line 64:
```cpp
if(0 == original_data_size)
    {
        PyErr_SetString(HashpumpError, "original_data is empty");
        return NULL;
    }
```
With these modifications, we can `make` to create the binary file and `python3 setup.py build` then `python3 setup.py install` to install the hashpumpy python library, which allows us to use HashPump inside a Python script.

All those modifications are already made on [my forked repo of HashPump](https://github.com/hhxn0x/HashPump) on my github profile, so feel free to clone this repo if you want a HashPump version already fixed.

Now that we have fixed our problem, we can solve the challenge.

Let's see an example of hashpump output:

```
hashpump -s "46eaafcb93f2c5f8fc215cac38e1eaaf" -d "" -a "my_user" -k 27

c59af6e67ad0d58ebc47a52c592c657d
\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd8\x00\x00\x00\x00\x00\x00\x00my_user
```

Here we can observe two results:
- The first one is our hash, which corresponds to `md5(secret + my_data)`
- The second one is the data we need to append to the secret. This means that in this case, `my_data = \x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd8\x00\x00\x00\x00\x00\x00\x00my_user`.

Now that we have all we need, we can create a new user on the web application. Its username will be the content of `my_data` and we can use any password. Then, we just log in with this username, the password we set at the registration and the hash that HashPump gave us and we should get the flag ! 

As the username is composed of bytes, it can be quite tricky to do that on a web browser but using burp or a python script allows us to do that quite easily.

```py
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
```
Output : 
```
adac276f4061a4b012fcbef12cdd3000 b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd8\x00\x00\x00\x00\x00\x00\x00n0x_'
<link rel="stylesheet" href="styles/style.css" type="text/css">
<div class="center">
  <h1>Welcome to the Site</h1>

      <p>Well done !</p>
    <p>Here is your flag : DVCTF{h4sh_l3ngth_3xt3ns1on_1s_funny} </p>
  </div>
```