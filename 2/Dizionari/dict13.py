# Leandro Gridelli

import random

def format_dict(d):
    for k in d:
        print(k, d[k] * "*")

# main

risultati = {}

volte = int(input("Quante volte vuoi lanciare: "))

for k in range(volte):
    somma = random.randint(1, 6) + random.randint(1, 6)
    
    if somma not in list(risultati.keys()):
        risultati[somma] = 1
    else:
        risultati[somma] += 1

format_dict(risultati)
