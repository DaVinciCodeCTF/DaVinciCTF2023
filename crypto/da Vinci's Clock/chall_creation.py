from Crypto.Cipher import AES
from hashlib import sha256
from Crypto.Util.number import getPrime, inverse, isPrime
from Crypto.Util.Padding import pad, unpad
import os
import random
import string

from collections import namedtuple
Point = namedtuple("Point", "x y")
O = 'Origin'

def check_point(P: tuple):
    if P == O:
        return True
    else:
        return (P.y**2 - (P.x**3 + a*P.x + b)) % p == 0 and 0 <= P.x < p and 0 <= P.y < p

def point_inverse(P: tuple):
    if P == O:
        return P
    return Point(P.x, -P.y % p)

def point_addition(P: tuple, Q: tuple):
    if P == O:
        return Q
    elif Q == O:
        return P
    elif Q == point_inverse(P):
        return O
    else:
        if P == Q:
            lam = (3*P.x**2 + a)*inverse(2*P.y, p)
            lam %= p
        else:
            lam = (Q.y - P.y) * inverse((Q.x - P.x), p)
            lam %= p
    Rx = (lam**2 - P.x - Q.x) % p
    Ry = (lam*(P.x - Rx) - P.y) % p
    R = Point(Rx, Ry)
    assert check_point(R)
    return R

def double_and_add(P: tuple, n: int):
    Q = P
    R = O
    r = 0
    while n > 0:
        if n % 2 == 1:
            R = point_addition(R, Q)
        Q = point_addition(Q, Q)
        n = n // 2
        r += 1
    assert check_point(R)
    return R

memory_file = open("memory_dump", "wb")
cipher = open("intercepted_message", 'w')

FLAG = b"7h3_Cl0ck_1s_71ck1n9!"

# secp256r1 -- P-256
p = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF
a = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFC
b = 0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B
G = Point(0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296, 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5)
n = 0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551

"""
leonard_private_key = n+1
while (leonard_private_key > n) :
    leonard_private_key = getPrime(256)
leonard_public_key = double_and_add(G,leonard_private_key)
my_private_key = int("1010000000100000001000000001",2)*(2**216) + 2*random.randint(1,2**215-1) + 1
while not(isPrime(my_private_key)) :
    my_private_key += 2
print(my_private_key)
"""

leonard_private_key = 100437665457807818500415257304045707893130424946425139206421043743314015525801
leonard_public_key = Point(x=31663442885885219669071274428005652588471134165143253841118506078548146970109, y=39635812297918732160112763208832215566025963497149555858771120961875750706113)

my_private_key = 17682328204146272905210039108115891745288961985724695248683935036009974579
my_public_key = double_and_add(G, my_private_key)

computing_time = 30*(my_private_key.bit_length() + my_private_key.bit_count() - 1) + 3 + random.random()

shared_secret_key = double_and_add(leonard_public_key, my_private_key).x

derived_aes_key = sha256(str(shared_secret_key).encode('ascii')).digest()
iv = os.urandom(16)
ciphertext = AES.new(derived_aes_key, AES.MODE_CBC, iv).encrypt(pad(FLAG,16,'pkcs7'))

cipher.writelines([str(my_public_key.x)+'\n', "You can be proud I can compute my message in less than {}ms".format(computing_time)+'\n', iv.hex()+'\n', ciphertext.hex()])

leak = hex(my_private_key)[9:]

def garbage(file, n) :
    alphabet = list(string.printable)[:-6]
    for k in range(1,n+1) :
        if 0.05 > random.random() :
            file.write(random.choice(alphabet).encode('ascii'))
        else :
            file.write(bytes(1))
        if k%32 == 0 :
            file.write('\n'.encode('ascii'))
    if n%32 :
        file.write('\n'.encode('ascii'))

def void(file, n) :
    for k in range(1,n+1) :
        file.write(bytes(1))
        if k%32 == 0 :
            file.write('\n'.encode('ascii'))

garbage(memory_file, 299)
void(memory_file, 32*2+17)
leak_format = [leak[k:k+2] if k%2 == 0 else ':' for k in range(-1,len(leak)-1)]
memory_file.write(("".join(leak_format[:15])+'\n').encode('ascii'))
memory_file.write(("".join(leak_format[15:47])+'\n').encode('ascii'))
memory_file.write(("".join(leak_format[47:])+'\n').encode('ascii'))
garbage(memory_file, 119)
garbage(memory_file, 369)
garbagee_key)
leak_format = [leak[k:k+8] if k%8 == 0 else ':' for k in range(0,len(leak)-4,4)]

garbage(memory_file, 299)
garbage(memory_file, 32*2+17)
for k in range(0,len(leak_format),32) :
    memory_file.write(("".join(leak_format[k:k+32])+'\n').encode('ascii'))
garbage(memory_file, 119)
garbage(memory_file, 369)
garbage(memory_file, 69)
