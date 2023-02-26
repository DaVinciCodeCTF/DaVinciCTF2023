message_xor = open("message", 'r').read()

# The first 5 letters gives 0 after the xor operation:
assert 5 == message_xor.index('1')//8

# Knowing the flag format, the message must start with "dvCTF" => the xor key starts with dvCTF for sure.
# What if we apply this key for the rest of the message (as a Vigenere key cipher but with the xor operation)
KEY = "dvCTF"
message = ""
for k in range(len(message_xor)//8) :
    message += chr(int(message_xor[8*k:8*(k+1)],2) ^ ord(KEY[k%5]))
print(message)
