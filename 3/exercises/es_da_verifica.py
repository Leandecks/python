# Leandro Gridelli

import random

def genera_stringa():
    alfabeto = "abcdefgilmnopqrstuvwz"
    stringa = ""
    for k in range(9):
        stringa += random.choice(alfabeto)
    return stringa

def vocali(stringa):
    v = "aeiou"
    contatore = 0
    for char in stringa:
        if char in v:
            contatore += 1
    return contatore

def is_primo(n):
    primo = True
    for k in range(2, n):
        if n % k == 0 and k != n:
            primo = False
    return primo

def nuova_stringa(stringa, is_primo):
    p = "0"
    if not is_primo:
        p = "1"
    return p + "_" + stringa

# main

file = open("vocali.txt", "w")
tot = 0

for k in range(10):
    stringa = genera_stringa()
    n_voc = vocali(stringa)
    tot += n_voc
    primo = is_primo(n_voc)
    nuova = nuova_stringa(stringa, primo)
    finale = nuova + "\t" + str(n_voc)
    file.write(finale + "\n")
    print(finale)

print("Totale vocali:", tot, ",è primo:", is_primo(tot))
file.close()
