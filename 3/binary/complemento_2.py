# Leandro Gridelli

def complemento(binario):
    invertito = ""
    for k in str(binario):
        if k == "0":
            invertito += "1"
        if k == "1":
            invertito += "0"
    print(invertito)

    print(bin(int(invertito, base = 2)))

    return bin(int(invertito, base = 2) + 1)

# main

n = int(input("Inserisci un binario: "))
print(complemento(n))
