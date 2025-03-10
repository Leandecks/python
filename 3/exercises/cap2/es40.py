# Leandro Gridelli

import random

while True:
    n = int(input("Inserire intero positivo: "))
    if n > 0 and type(n) == int:
        break
        
c = 0

for k in range(n):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    if dado1 > dado2:
        c += 1

print(f"Dado 1 maggiore di dado 2 {c} volte")
