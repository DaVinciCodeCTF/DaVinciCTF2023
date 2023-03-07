from Crypto.Util.number import isPrime, GCD
from functools import reduce
import random
import math

# Was lazy, didn't automate it in pwntools

primes = []
def sieve(maximum=10000):
    marked = [False]*(int(maximum/2)+1)
    for i in range(1, int((math.sqrt(maximum)-1)/2)+1):
        for j in range(((i*(i+1)) << 1), (int(maximum/2)+1), (2*i+1)):
            marked[j] = True
    primes.append(2)
    for i in range(1, int(maximum/2)):
        if (marked[i] == False):
            primes.append(2*i + 1)
sieve()
primes = primes[:500]

"""
n = 1491
p_smooth = 0
median = primes[len(primes)//2].bit_length()-1
nbr_of_primes = n//median
while p_smooth.bit_length() < n or not(isPrime(p_smooth)) :
    p_smooth = reduce(lambda x,y : x*y, random.sample(primes, k = nbr_of_primes))+1
"""

p_smooth = 154719943404171706604055732251563060479136515199754584923158109616046965037403706912398998212500126962484188969489865697961198671730865525225579264093752879315061093864733298804493722100527126346446902826292113345359383149782517099170605786436734077706528358759955851236316464073656862744783612663937811733466979300836872639011440620076402042668742786709631716674939802328016376569720503727691131438751004085673243322211337645924770637325271424364027
assert p_smooth.bit_length() == 1493

"""
You receive first the variables A,B,g,p,iv and message sent during their exchange.

You send: {"g": 2, "A": <the A given by Leonard>, "p": p_smooth}
You receive a second B calculated with this modulus.

To retrieve the private key of Leonard's friend (privkey):
run: python3 Pohlig_Hellman.py -g 2 -A <B> -p <p_smooth>

To decipher the message:
private_key = pow(<A>,<privkey>,<p>)
run: python3 decrypt.py -k <private_key> -iv <iv> -c <message>
"""

