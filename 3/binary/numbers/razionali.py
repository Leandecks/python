# Leandro Gridelli

def binario(b):
    return bin(int(b))

def binario_raz(b):
    b = str(b).split(".")
    print(f"Parte intera: {b[0]}")
    print(f"Parte razionale: {b[1]}")
    intera = binario(int(b[0]))
    decimale = ""
    n = float("0." + b[1])
    contatore = 0
    while n * 2 != 1:
        contatore += 1
        n *= 2
        if contatore > 100:
            break
        if n > 1:
            n = float("0." + str(n).split(".")[1])
            decimale += "1"
        else:
            decimale += "0"
    decimale += "1"
    return intera.strip("0b") + "." + decimale

# main

razionale = float(input("Inserisci razionale: "))
print(f"Numero in binario: {binario_raz(razionale)}")