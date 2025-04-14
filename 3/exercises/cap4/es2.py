# Leandro Gridelli

import random

with open("cognomi.txt") as file:
    cognomi = []
    
    for riga in file:
        cognomi.append(riga.strip("\n"))

voti = []

for cognome in cognomi:
    lista_voti = []
    lista_voti.append(cognome)
    
    for i in range(5):
        voto = random.randint(0, 10)
        lista_voti.append(voto)
        
    print(lista_voti)
        