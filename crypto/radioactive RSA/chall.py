from Crypto.Util.number import getStrongPrime, inverse, GCD, bytes_to_long
import random
import hashlib

FLAG = b"[REDACTED]"

e = 0x10001
while True:
    p = getStrongPrime(2048)
    q = getStrongPrime(2048)
    phi = (p-1)*(q-1)
    d = inverse(e, phi)
    if d > 1 and GCD(e, phi) == 1:
        break

N = p * q
ct = pow(bytes_to_long(FLAG),e,N)

print(N)
print(e)
print(ct)

d2 = bin(d ^ int(bin(d)[2:][::-1],2))[2:].zfill(4096)
d2_blocs = [d2[k*4096//8:(k+1)*4096//8] for k in range(8)]
d2_mixed_up = [None] * 8
mix_order = ""
while None in d2_mixed_up :
    r = random.randint(0,7)
    if d2_mixed_up[r] :
        r = random.randint(0,7)
    if not d2_mixed_up[r] :
        d2_mixed_up[r] = d2_blocs.pop()
    mix_order += '-'+str(r) if mix_order else str(r)
mix_protection_hash = hashlib.md5()
mix_protection_hash.update(mix_order.encode('ascii'))

print("".join(d2_mixed_up))
print("{}:{}".format(len(mix_order)//2+1, mix_protection_hash.hexdigest()))
