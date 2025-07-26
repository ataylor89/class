import sys
import pickle

if len(sys.argv) != 2:
    print("Usage: python xor.py <filename>")
    sys.exit(0)

filename = sys.argv[1]
file = open(filename, "r")
message = file.read()
cipher = ""

file = open("key.txt", "rb")
key = pickle.load(file)
keylen = len(key)

for i in range(0, len(message)):
    m = ord(message[i])
    k = key[i % keylen]
    c = chr(m ^ k)
    cipher += c

print(cipher, end='')
