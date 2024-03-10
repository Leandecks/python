# Leandro Gridelli

import math

def cfr(r):
    return 2 * r * math.pi

def cerchio(r):
    return r**2 * math.pi

# main

r = int(input("Inserisci il raggio: "))

print(f"Circonferenza: {cfr(r)}")
print(f"Cerchio: {cerchio(r)}")