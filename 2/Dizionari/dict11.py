# Leandro Gridelli

import random

# main

risultati = {
    "Testa": 0,
    "Croce": 0
}

volte = int(input("Quante volte vuoi lanciare: "))

for k in range(volte):
    moneta = random.randint(0, 1)
    if moneta == 0:
        risultati["Testa"] += 1
    else:
        risultati["Croce"] += 1

print(risultati)
