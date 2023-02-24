from PIL import Image
import random
import math

FLAG = b"dvCTF{[REDACTED]}"
LSB = "".join([format(l,'b').zfill(8) for l in FLAG]).zfill(24*math.ceil(len(FLAG)/3))

leonards_image = Image.open("Leonards_image.png")
mode, (columns, rows) = leonards_image.mode, leonards_image.size
half, size = columns+rows, columns*rows

message = Image.new(mode, (columns, rows))

for r in range(rows) :
    for c in range(columns) :
        pixel = tuple((val+random.randint(0,1))%256 for val in leonards_image.getpixel((c,r))[:3])
        message.putpixel((c,r), pixel)

z = size
while len(FLAG) > 3*(size-z)//(8*4*100) :
    starting_point = (random.randint(0,columns-1),random.randint(0,rows-1))
    z = starting_point[0] + starting_point[1]*columns
for k in range(0,len(LSB),3) :
    z = z + random.randint(1,4)*100
    point = (z%columns, z//columns)
    val = tuple(pixel&254+int(LSB[k+i]) for (i,pixel) in list(enumerate(message.getpixel(point)))[:3])

print(point)
message.save("message.png")
