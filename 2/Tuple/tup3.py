# Leandro Gridelli

import random


def genera_calciatori(n):
    calciatori = []

    for k in range(n):
        nome = input("Inserisci un calciatore: ")
        calciatori.append(nome)

    return calciatori


def genera_presenze(n):
    presenze = []

    for k in range(n):
        presenza = random.randint(10, 38)
        presenze.append(presenza)

    return presenze


def genera_goal(n):
    presenze = []

    for k in range(n):
        presenza = random.randint(3, 20)
        presenze.append(presenza)

    return presenze


def genera_giudizio(rapporto):
    if rapporto > 1:
        return "Ottimo"
    elif rapporto > 0.6 and rapporto < 1:
        return "Buono"
    elif rapporto > 0.3 and rapporto < 0.6:
        return "Sufficiente"
    elif rapporto > 0.1 and rapporto < 0.3:
        return "Insufficiente"
    else:
        return "Scarso"


# Main

calciatori = {}

# nomi = genera_calciatori(10)
nomi = ['Juri', 'Crine', 'Capo', 'Michi', 'Thomas', 'Michael', 'Giova', 'Clara', 'Vitto', 'Bondo']
presenze = genera_presenze(10)
goal = genera_goal(10)

for k in range(10):
    nome = nomi[k]
    presenza = presenze[k]
    g = goal[k]
    presenze_su_goal = round(presenza / g, 2)
    giudizio = genera_giudizio(presenze_su_goal)

    valore = (presenza, g, presenze_su_goal, giudizio)

    calciatori[nome] = valore

# Output Diz

print(f"I calciatori sono: {nomi}")
print(f"Presenze: {presenze}")
print(f"Goal: {goal}")

print()

for giocatore in calciatori:
    print(giocatore + "\t\t", end="")

    for el in calciatori[giocatore]:
        print(str(el) + "\t\t", end="")

    print()

print("\n")

# Output Giudizi

giudizi = {}

for g in ["Ottimo", "Buono", "Sufficiente", "Insufficiente", "Scarso"]:
    print(g + ":")
    for giocatore in calciatori:
        if g == calciatori[giocatore][3]:
            print(giocatore)

    print()
