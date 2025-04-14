# Leandro Gridelli

import random

cognomi = ["bartolini", "gonzalez", "giacomini", "benvenuti", "clementi", "collini", "maioli", "berardi", "franco", "magnani", "scornavacche", "sacchini", "viarani", "ferrari", "pavolucci", "gridelli", "sacchetti", "pompili", "matteo"]
# 20

x = int(input("Inserire numero di persone per gruppo (da 3 a 5): "))

disordine = []

while len(disordine) != len(cognomi):
    persona = random.choice(cognomi)
    while persona in disordine:
        persona = random.choice(cognomi)
    disordine.append(persona)

gruppi = []
gruppo = []

for i in range(len(disordine)):
    el = disordine[i]
    
    gruppo.append(el)
    
    if len(gruppo) == x:
        gruppi.append(gruppo)
        gruppo = []
    
    if i == len(disordine) - 1:
        gruppi.append(gruppo)

print(gruppi)
