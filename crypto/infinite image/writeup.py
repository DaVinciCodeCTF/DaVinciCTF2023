from PIL import Image
import string

message_image = Image.open("message.png")
(columns, rows) = message_image.size
last_point = eval(open("message",'r').read())

def LSB_from_pixel(point : tuple[int,int]) -> str :
    return "".join((str(val%2) for val in message_image.getpixel(point)[:3]))

authorized_values = set(ord(l) for l in string.ascii_lowercase + string.digits + 'CTF_}{')
def good_24series(serie : str) -> bool :
    serie = [int(serie[k:k+8],2) for k in range(0,24,8)]
    if serie[0] == 0 and chr(serie[1]) == 'd' and chr(serie[2]) == 'v' :
        return True
    if serie[0] == serie[1] == 0 and serie[2] == 'd' :
        return True
    else :
        return all(val in authorized_values for val in serie)

def add_next_point(binaries : set[tuple[str,int]]) -> set[tuple[str,int]] :
    res = binaries.copy()
    for binary,z in binaries :
        next_z = [z-k*100 for k in range(1,3)]
        res.discard((binary,z))
        for zz in next_z :
            res.add((LSB_from_pixel((zz%columns, zz//columns))+binary, zz))
    return res

def next_3_letters(z:int, end=False) -> set[tuple[str,int]] :
    if end :
        possibles = {(LSB_from_pixel((z%columns, z//columns)),z)}
    else :
        possibles = {("",z)}
    for k in range(8-end) :
        possibles = add_next_point(possibles)
    res = set()
    for binary,z in possibles :
        if good_24series(binary) :
            res.add(("".join(chr(val) for val in [int(binary[k:k+8],2) for k in range(0,24,8)] if val in authorized_values),z))
    return res




        

