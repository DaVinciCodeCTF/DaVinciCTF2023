message_xor = open("message", 'r').read()
assert len(message_xor)//8 == len(message_xor)/8

# The first 6 letters are known "dvCTF{" so we can retrieve the first 6 letters of the xor key:
start = 'dvCTF{'
KEY = "".join(chr(int(message_xor[k*8:8*(k+1)],2) ^ ord(start[k])) for k in range(6))
print(KEY)

# What if we apply this key for the rest of the message (as a Vigenere key cipher but with the xor operation)
message = ""
for k in range(len(message_xor)//8) :
    message += chr(int(message_xor[8*k:8*(k+1)],2) ^ ord(KEY[k%len(KEY)]))
print(message)
