import random
import pickle

keylen = 1024
key = []
for i in range(0, keylen):
    key.append(random.randint(0, 255))

with open("key.txt", "wb") as file:
    pickle.dump(key, file)
