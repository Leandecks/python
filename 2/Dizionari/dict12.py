# Leandro Gridelli

import random

def format_dict(d):
    for k in d:
        print(k, d[k])

# main

risultati = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}

volte = int(input("Quante volte vuoi lanciare: "))

for k in range(volte):
    dado = random.randint(1, 6)
    risultati[dado] += 1

format_dict(risultati)
