FLAG = "dvCTF{80R3D_K3Y_15_K3Y_MY_FR13ND}"
KEY = "dvCTF"
message = ""
for k in range(len(FLAG)) :
    message += bin(ord(FLAG[k]) ^ ord(KEY[k%5]))[2:].zfill(8)

message_file = open("message",'w')
message_file.write(message)

