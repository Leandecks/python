# Leandro Gridelli

import unicodedata

def utf32(x):
    x = str(bin(x)).strip("0b")
    if len(x) < 32:
        x = (32 - len(x)) * "0" + x
    return x[:16] + " " + x[16:]

# main

n = int(input("Numero compreso fra 0 e 1.048.576: "))
print(f"Code point: U+{str(hex(n)).strip('0x')}")
print(f"Glifo: {chr(n)}")
print(f"Descrizione: {unicodedata.name(chr(n))}")
print(f"UTF-32: {utf32(n)}")
