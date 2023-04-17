# Leandro Gridelli

import random

uno = random.randint(1,6)
due = random.randint(1,6)
tre = random.randint(1,6)

somma = uno + due + tre

print(f"Lancio dadi: {uno} {due} {tre}")
print(f"Somma: {somma:02d}")

if somma >= 15:
    print("Vinci 3 euro")
else:
    if somma >= 10:
        print("Vinci 1 euro")
    else:
        print("Perdi 1 euro")
