# Leandro Gridelli

import random

with open("cognomi.txt") as file:
    cognomi = []
    
    for riga in file:
        cognomi.append(riga.strip("\n"))

voti = []

for cognome in cognomi:
    lista_voti = [cognome]

    for i in range(5):
        voto = random.randint(0, 10)
        lista_voti.append(voto)

    voti.append(lista_voti)

for studente in voti:
    print(studente)
    print(f"Studente: {studente[0]}, voto massimo: {max(studente[1:])}, voto minimo: {min(studente[1:])}, media: {sum(studente[1:]) / 5}")
