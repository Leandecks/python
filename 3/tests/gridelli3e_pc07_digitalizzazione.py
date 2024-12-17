# Gridelli Leandro PC07 Digitalizzazione

import random

def genera_sequenza():
    seq = ""
    
    for k in range(3):
        for k in range(8):
            seq += str(random.randint(0, 1))
        seq += " "
    
    return seq

def conta_uno(seq):
    contatore = 0
    for char in seq:
        if char == "1":
            contatore += 1
    return str(contatore).zfill(2)

def bit_multipli(nr):
    resto = int(nr) % 3
    if resto == 1:
        return "11"
    elif resto == 2:
        return "10"
    else:
        return "00"

def su_file(txt):
    file = open("dati.txt", "w")
    file.write(txt)
    file.close()

# main

testo = ""

for k in range(10):
    sequenza = genera_sequenza()
    nr_uno = conta_uno(sequenza)
    finale = bit_multipli(nr_uno)
    riga = f"{sequenza}- {nr_uno} - {finale}"
    print(riga)
    testo += riga + "\n"
    su_file(testo)
