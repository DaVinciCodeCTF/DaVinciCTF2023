from PIL import Image
import hashlib
import random
import math

FLAG = b"dvCTF{W3lc0m3_4ll_T0_Cr9pt0gr4ph9}"
LSB = "".join([format(l,'b').zfill(8) for l in FLAG]).zfill(8*3*math.ceil(len(FLAG)/3))

leonards_image = Image.open("Leonards_image.png")
message = Image.new(leonards_image.mode, leonards_image.size)
(columns, rows) = leonards_image.size
size = columns*rows

# Add noise to the image
def create_and_add_noise() :
    for r in range(rows) :
        for c in range(columns) :
            pixel = tuple((val+random.randint(0,1))%256 for val in leonards_image.getpixel((c,r))[:3])
            message.putpixel((c,r), pixel)

z = size
while 1000*8*len(FLAG)//3 + z >= size :
    z = random.randint(0,size-1)
# LSB on pseudo-random points
def LSB_encrypt(start = z) :
    LSB_points = []
    for k in range(len(LSB)//6) :
        start += random.choice((1,5,10))*100 + 1
        LSB_points += [start-1,start]
    for k,point in enumerate(LSB_points) :
        position = (point%columns,point//columns)
        pixel = tuple(((p&254)+int(LSB[3*k+i])) for (i,p) in list(enumerate(message.getpixel(position)))[:3])
        message.putpixel(position,pixel)
    return position

create_and_add_noise()
last_point = LSB_encrypt()
leonards_image.close()

flag_hash = hashlib.md5()
flag_hash.update(FLAG)

message.save("message.png") # Saving the LSB message image
message.close()

message_file = open("message", 'w')
message_file.write(str(last_point)+' : '+flag_hash.hexdigest()) # Saving the last point
message_file.close()
