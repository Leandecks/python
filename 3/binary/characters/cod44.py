# Leandro Gridelli

import random
import unicodedata
from encodings import undefined


def utf16(x):
    x = str(bin(x)).strip("0b")
    if len(x) < 16:
        x = (16 - len(x)) * "0" + x
    return x[:8] + " " + x[8:]

# main

n = random.randint(0, 65535)

if int(0xd800) <= n <= int(0xdbff):
    print("High surrogate")
elif int(0xdc00) <= n <= int(0xdfff):
    print("Low surrogate")
else:
    print(f"Code point: U+{str(hex(n)).strip('0x')}")
    print(f"Glifo: {chr(n)}")
    try:
        print(f"Descrizione: {unicodedata.name(chr(n))}")
    except ValueError:
        print("Carattere non definito")
    print(f"UTF-16: {utf16(n)}")