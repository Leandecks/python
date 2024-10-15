# Leandro Gridelli

def complemento_1(s):
    stringa = ""
    for k in s:
        if k == "0":
            stringa += "1"
        if k == "1":
            stringa += "0"
    return bin(int(stringa, base = 2))

def somma_binari(x, y):
    return bin(int(x, base = 2) + int(y, base = 2))

def complemento_2(s):
    return somma_binari(complemento_1(s), "0001")

# main

print(f"Il complemento a 1 di 1001 è {complemento_1('1001')}")
print(somma_binari("0010", "0010"))
print(complemento_2("11101011"))
