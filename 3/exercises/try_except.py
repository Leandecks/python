import unicodedata
import random

try:
    print(unicodedata.name(chr(random.randint(0, 100000))))
except ValueError:
    print("doesnt exist")
