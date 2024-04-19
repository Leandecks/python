# Leandro Gridelli

import random

# main

amici = {}

for k in range(4):
    amico = input("Immetti nome: ")
    telefono = str(random.randint(200, 400)) + str(random.randint(1000000, 9999999))

    amici[amico] = telefono

for amico in amici:
    print(amico, ": numero = ", amici[amico])
