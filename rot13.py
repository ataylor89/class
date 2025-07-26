import sys

def rot13(msg):
    cipher = ""
    for c in msg:
        if c >= 'a' and c <= 'z':
            pos = ord(c) - ord('a')
            pos = (pos + 13) % 26
            code = ord('a') + pos
            cipher += chr(code)
        elif c >= 'A' and c <= 'Z':
            pos = ord(c) - ord('A')
            pos = (pos + 13) % 26
            code = ord('A') + pos
            cipher += chr(code)
        else:
            cipher += c
    return cipher

if len(sys.argv) != 2:
    print("Usage: python rot13.py <filename>")
    sys.exit(0)

filename = sys.argv[1]
file = open(filename, "r")
msg = file.read()
cipher = rot13(msg)
print(cipher, end='')
