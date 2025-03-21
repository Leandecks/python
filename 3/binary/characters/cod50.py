# Leandro Gridelli

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

frase = input("Inserisci frase: ")

u32 = ""
u16 = ""
u8 = ""

for char in frase:
    char = ord(char)
    u32 += utf32(char) + " "
    u16 += utf16(char) + " "
    u8 += utf8(char) + " "

print(u32)
print()
print()
print()
print(u16)
print()
print()
print()
print(u8)
