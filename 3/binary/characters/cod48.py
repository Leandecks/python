# Leandro Gridelli
import unicodedata

def desc(p):
    try:
        unicodedata.name(chr(p))
    except ValueError:
        return "Inesistente"

def utf32(n):
    n = str(bin(n))[2:]
    n = n.zfill(32)
    result = ""
    for k in range(len(n)):
        if k % 8 == 0:
            result += " "
        result += n[k]

    return result

def utf16(n):
    if n > 2 ** 16:
        return "Troppo alto"
    n = str(bin(n))[2:]
    n = n.zfill(16)
    result = ""
    for k in range(len(n)):
        if k % 8 == 0:
            result += " "
        result += n[k]

    return result

def utf8(n):
    if n < 2 ** 7: # 0xxxxxxx
        return "0" + str(bin(n))[2:].zfill(7)
    elif n < 2 ** 11: # 110xxxxx 10xxxxxx
        caso2 = str(bin(n))[2:].zfill(11)
        return "110" + caso2[:5] + " 10" + caso2[5:]
    elif n < 2 ** 16: # 1110xxxx 10xxxxxx 10xxxxxx
        caso3 = str(bin(n))[2:].zfill(16)
        return "1110" + caso3[:4] + " 10" + caso3[4:10] + " 10" + caso3[10:]
    else: # 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
        caso4 = str(bin(n))[2:].zfill(21)
        return "11110" + caso4[:3] + " 10" + caso4[3:9] + " 10" + caso4[9:15] + " 10" + caso4[15:]

# main

cp = "0x" + input("Inserisci codepoint: ")[2:]
pos = int(cp, 16)
print(f"Hex: {cp}")
print(f"Glifo: {chr(pos)}")
print(f"Descrizione: {desc(pos)}")
print(f"UTF-32: {utf32(pos)}")
print(f"UTF-16: {utf16(pos)}")
print(f"UTF-8: {utf8(pos)}")
