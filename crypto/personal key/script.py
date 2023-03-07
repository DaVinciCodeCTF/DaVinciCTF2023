from Crypto.Util.number import getPrime, isPrime
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import hashlib
import random
import json
import os

FLAG = b"dvCTF{0M6_1_5h0u1d_Ch4n63_M9_K39_F0r_34ch_3xch4n63!}"
DVC_banner = r"""
 _______           __     __ __                   __  ______                 __          
|       \         |  \   |  \  \                 |  \/      \               |  \         
| ▓▓▓▓▓▓▓\ ______ | ▓▓   | ▓▓\▓▓_______   _______ \▓▓  ▓▓▓▓▓▓\ ______   ____| ▓▓ ______  
| ▓▓  | ▓▓|      \| ▓▓   | ▓▓  \       \ /       \  \ ▓▓   \▓▓/      \ /      ▓▓/      \ 
| ▓▓  | ▓▓ \▓▓▓▓▓▓\\▓▓\ /  ▓▓ ▓▓ ▓▓▓▓▓▓▓\  ▓▓▓▓▓▓▓ ▓▓ ▓▓     |  ▓▓▓▓▓▓\  ▓▓▓▓▓▓▓  ▓▓▓▓▓▓\
| ▓▓  | ▓▓/      ▓▓ \▓▓\  ▓▓| ▓▓ ▓▓  | ▓▓ ▓▓     | ▓▓ ▓▓   __| ▓▓  | ▓▓ ▓▓  | ▓▓ ▓▓    ▓▓
| ▓▓__/ ▓▓  ▓▓▓▓▓▓▓  \▓▓ ▓▓ | ▓▓ ▓▓  | ▓▓ ▓▓_____| ▓▓ ▓▓__/  \ ▓▓__/ ▓▓ ▓▓__| ▓▓ ▓▓▓▓▓▓▓▓
| ▓▓    ▓▓\▓▓    ▓▓   \▓▓▓  | ▓▓ ▓▓  | ▓▓\▓▓     \ ▓▓\▓▓    ▓▓\▓▓    ▓▓\▓▓    ▓▓\▓▓     \
 \▓▓▓▓▓▓▓  \▓▓▓▓▓▓▓    \▓    \▓▓\▓▓   \▓▓ \▓▓▓▓▓▓▓\▓▓ \▓▓▓▓▓▓  \▓▓▓▓▓▓  \▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓
                                                                                         
                                                                                         
"""

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 
    127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 
    179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 
    233, 239, 241, 251, 257, 263, 269, 271, 277, 281]

a,b,A,B,g,p = 0,0,0,0,0,0
def create_chall(n = 1500) :
    global a,b,A,B,g,p
    """
    while not(isPrime(p)) :
        p2 = getPrime(n//9)*getPrime(n//9)*getPrime(n//9)*getPrime(n//9)*getPrime(n//9)*getPrime(n//9)*getPrime(n//9)*getPrime(n//9)*getPrime(n//9)
        for prime in primes :
            p = prime*p2 + 1
            if isPrime(p) :
                break
    """
    p = 67909058639015901521159994775573035383954459487261606166344237532826148072679017733601374658223148561768415561603664175917512048376819174420250853454732953324581854497582753829708301928284664779076154088688830021115279512578857692227479562674882071152106576596875913352557789324670379649786609825434409435255821942736505342286648408198244821312692516037516042858869576975348446692782484818336732578529321186507590599512517447475812534029481702096279
    g = 2 # p = 2 * very_big_primes
    """
    b = p+1
    while (b>p) :
        for k in range(3) :
            b = getPrime(p.bit_length())
    """
    a, b = 1, 65473639808699485930169739120776344872063486759175448375528264725076385240507007122033725140840484612862406919640595260700686522495480907572356389076167853197821801826383447351648059986031889813351817873001488294494701722629749684148909427325850459979675565503434023079995359625609088269771844354760835818954684415257284162502387237305785209643574211555375172193651636111175028374996815892412132272802165727822181091506346864627612264559401722904573
    for k in range(4) :
        a = a*random.choice(primes[2:])*random.randint(1,2**(p.bit_length()//4))
    a = a//(2**(a.bit_length()-p.bit_length()))
    assert a<p-1
    
    A = pow(g,a,p)
    B = pow(g,b,p)

def chall_initialization() :
    private_key = pow(g,a*b,p)
    derived_aes_key = hashlib.sha256(str(private_key).encode('ascii')).digest()
    iv = os.urandom(16).hex()
    cipher = AES.new(derived_aes_key, AES.MODE_CBC, bytes.fromhex(iv))
    message = cipher.encrypt(pad(FLAG,16,'pkcs7')).hex()
    
    sent_by_Leonard = {"A":A, "g":g, "p":p}
    sent_by_his_friend = {"B":B, "iv":iv, "message":message}
    
    print(DVC_banner)
    print("From Leonard:\n{}\n".format(sent_by_Leonard))
    print("From his friend:\n{}\n".format(sent_by_his_friend))

def format(user_input : str) -> tuple[int,int,int]:
    usage = 'The accepted format is a dictionnary in json format: {"A": <integer>, "g": <integer>, "p": <integer>}'

    try :
        json_load = json.loads(user_input)
        return json_load['A'],json_load['g'],json_load['p']
    except Exception:
        return f"Bad json formatting.\n"+usage

def check_and_return(A_user : int, g_user : int, p_user : int) :
    if g_user != g :
        return "I always use g=2, so please do the same like usual."
    if A_user != A :
        return "How can this be, you don't have the same public key than before. It shouldn't be possible!"
    if p_user < A :
        return "p is smaller than A"
    if not(isPrime(p_user)) :
        return "p isn't prime!"
    if (p_user.bit_length() - A.bit_length()) > 16 :
        return "p doesn't seem legit, it's too big compared to A."
    return {'B':pow(g,b,p_user)}

def chall() :
    user_input = input()
    value_received = format(user_input)
    if isinstance(value_received, str) :
        print(value_received+'\n')
    else :
        A_user, g_user, p_user = value_received
        print("Received from his friend:\n{}\n".format(check_and_return(A_user, g_user, p_user)))

def main() :
    create_chall()
    chall_initialization()
    print('You can now speak with Leonard\'s friend: the accepted format is a dictionnary in json format: {"A": <integer>, "g": <integer>, "p": <integer>}')
    chall()

if __name__ == '__main__':
    main()
