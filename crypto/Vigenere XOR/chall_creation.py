
FLAG = "You did it! The flag is dvCTF{80R3D_K3Y_15_K3Y_MY_FR13ND}. Well done !"
KEY = "CR9PT0"
message = ""
for k in range(len(FLAG)) :
    message += bin(ord(FLAG[k]) ^ ord(KEY[k%len(KEY)]))[2:].zfill(8)

message_file = open("message",'w')
message_file.write(message)
