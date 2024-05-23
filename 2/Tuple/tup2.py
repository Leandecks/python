# Leandro Gridelli

import random


def genera_mazzo(n):
    mazzo = []
    semi = ["b", "d", "s", "c"]

    # Generazione

    for k in range(n):
        numero = random.randint(1, 10)
        seme = random.choice(semi)

        carta = (numero, seme)

        mazzo.append(carta)

    return mazzo


def carte_uniche(mazzo):
    carte_uniche = {}

    for carta in mazzo:
        if carta not in list(carte_uniche.keys()):
            carte_uniche[carta] = 1
        else:
            carte_uniche[carta] += 1

    return carte_uniche


def dieci_volte(carte):
    dieci_volte = []

    for carta in carte:
        if carte[carta] == 10:
            dieci_volte.append(carta)

    return dieci_volte


def quindici_volte(carte):
    quindici_piu = []

    for carta in carte:
        if carte[carta] > 15:
            quindici_piu.append(carta)

    return quindici_piu


def estratte_piu(carte):
    ordine = {}
    quantita = sorted(carte.values())[-10:]

    for q in quantita:
        for c in carte:
            if carte[c] == q:
                ordine[c] = carte[c]

    return ordine


def esatte_carte_mai_estratte(mazzo_totale, mazzo_uniche):
    uniche_tot = list(mazzo_totale.keys())

    non_estratte_60 = []

    for carta_unica in uniche_tot:
        if carta_unica not in mazzo_uniche:
            non_estratte_60.append(carta_unica)

    return non_estratte_60


# Main

mazzo = genera_mazzo(500)

# Carte mai estratte

carte_mai_estratte = carte_uniche(mazzo)
print(f"Carte mai estratte: {40 - len(carte_mai_estratte)}")

# Carte estratte 10 volte

dieci = dieci_volte(carte_mai_estratte)

print(f"Carte estratte 10 volte: {dieci}")

# Carte estratte più di 15 volte

quindici_piu = quindici_volte(carte_mai_estratte)
print(f"Carte estratte più di 15 volte: {quindici_piu}")

# 10 carte estratte più volte

ordinate = estratte_piu(carte_mai_estratte)
print(f"10 carte piu estratte in ordine: {ordinate}")

# Quali mai estratte

mazzo_60 = genera_mazzo(60)
uniche_60 = carte_uniche(mazzo_60)
mai_estratte_60 = esatte_carte_mai_estratte(carte_mai_estratte, uniche_60)

print(f"Carte mai estratte da nuovo mazzo di 60 carte: {mai_estratte_60}")
