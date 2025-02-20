# Leandro Gridelli

# Il programma determina se una matrice è a spirale o no. Funzione: is_matrice(matrice)

####################### ALGORITMI GENERALI ##################################


def matrix(lato):
    m = []

    for x in range(lato):
        r = []
        for y in range(lato):
            r.append(0)
        m.append(r)

    return m


def print_matrice(matrice):
    for riga in matrice:
        for valore in riga:
            print(valore, end="\t")
        print()


def inverti_matrice(matrice):
    """
    ALGORITMO INVERTIMATRICE

    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]

    m[2][1] -> m[1][2]

    diventa

    [1, 8, 7],
    [2, 9, 6],
    [3, 4, 5]

    """
    nuova = matrix(len(matrice))

    for x in range(len(nuova)):
        for y in range(len(nuova[x])):
            nuova[x][y] = matrice[y][x]

    return nuova


######################### ALGORITMI DI DIREZIONE ################################


def destra(matrice, elemento_attuale):
    """
    ALGORITMO DESTRA

    > parti dalla prima cella vuota da sinistra
    > riempi le celle vuote verso DESTRA
    > riempi partendo dall'elemento attuale della lista degli elementi
    > smetti quando la cella che incontri è piena
    """

    finito = False

    riga_da_scrivere = []
    numero_riga = 0
    c = -1

    for riga in matrice:
        c += 1
        if 0 not in riga:
            continue
        riga_da_scrivere = riga
        numero_riga = c
        break

    if riga_da_scrivere == []:
        finito = True
        return matrice, elemento_attuale, finito

    for indice in range(len(riga_da_scrivere)):
        if riga_da_scrivere[indice] != 0:
            continue
        riga_da_scrivere[indice] = elemento_attuale
        elemento_attuale += 1

    matrice[numero_riga] = riga_da_scrivere

    return matrice, elemento_attuale, finito


def giu(matrice, elemento_attuale):
    """
    ALGORITMO GIU
    > parti dalla prima cella vuota dall'alto
    > riempi le celle vuote verso il BASSO
    > riempi partendo dall'elemento attuale della lista degli elementi
    > smetti quando la cella che incontri è piena
    """

    finito = False

    matrice = inverti_matrice(matrice)
    numero_colonna = 0
    c = len(matrice)

    colonna_da_scrivere = []

    for colonna in reversed(matrice):
        c -= 1
        if 0 not in colonna:
            continue
        colonna_da_scrivere = colonna
        numero_colonna = c
        break

    if colonna_da_scrivere == []:
        finito = True
        return inverti_matrice(matrice), elemento_attuale, finito

    for indice in range(len(colonna_da_scrivere)):
        if colonna_da_scrivere[indice] != 0:
            continue
        colonna_da_scrivere[indice] = elemento_attuale
        elemento_attuale += 1


    matrice[numero_colonna] = colonna_da_scrivere

    return inverti_matrice(matrice), elemento_attuale, finito


def sinistra(matrice, elemento_attuale):
    """
    ALGORITMO SINISTRA
    > parti dalla prima cella vuota da destra
    > riempi le celle vuote verso SINISTRA
    > riempi partendo dall'elemento attuale della lista degli elementi
    > smetti quando la cella che incontri è piena
    """

    finito = False

    riga_da_scrivere = []
    numero_riga = 0
    c = len(matrice)

    for riga in reversed(matrice):
        c -= 1
        if 0 not in riga:
            continue
        riga_da_scrivere = list(reversed(riga))
        numero_riga = c
        break

    if riga_da_scrivere == []:
        finito = True
        return matrice, elemento_attuale, finito

    for indice in range(len(riga_da_scrivere)):
        if riga_da_scrivere[indice] != 0:
            continue
        riga_da_scrivere[indice] = elemento_attuale
        elemento_attuale += 1

    matrice[numero_riga] = list(reversed(riga_da_scrivere))

    return matrice, elemento_attuale, finito


def su(matrice, elemento_attuale):
    """
    ALGORITMO SU
    > parti dalla prima cella vuota dal basso
    > riempi le celle vuote verso l'ALTO
    > riempi partendo dall'elemento attuale della lista degli elementi
    > smetti quando la cella che incontri è piena
    """

    finito = False

    matrice = inverti_matrice(matrice)
    numero_colonna = 0
    c = -1

    colonna_da_scrivere = []

    for colonna in matrice:
        c += 1
        if 0 not in colonna:
            continue
        colonna_da_scrivere = list(reversed(colonna))
        numero_colonna = c
        break

    if colonna_da_scrivere == []:
        finito = True
        return inverti_matrice(matrice), elemento_attuale, finito

    for indice in range(len(colonna_da_scrivere)):
        if colonna_da_scrivere[indice] != 0:
            continue
        colonna_da_scrivere[indice] = elemento_attuale
        elemento_attuale += 1

    matrice[numero_colonna] = list(reversed(colonna_da_scrivere))

    return inverti_matrice(matrice), elemento_attuale, finito


def fill_matrix(lato):
    matrice = matrix(lato)
    elementi = []
    elemento_attuale = 0
    gruppo_attuale = 0

    for a in range(1, lato ** 2 + 1):
        elementi.append(a)

    for valore in matrice[gruppo_attuale]:
        for b in range(lato):
            matrice[gruppo_attuale][b] = elementi[elemento_attuale]
            elemento_attuale += 1


def genera_matrice(lato):
    matrice = matrix(lato)
    elemento_attuale = 1

    while True:
        matrice, elemento_attuale, finito = destra(matrice, elemento_attuale)
        if finito:
            break

        matrice, elemento_attuale, finito = giu(matrice, elemento_attuale)
        if finito:
            break

        matrice, elemento_attuale, finito = sinistra(matrice, elemento_attuale)
        if finito:
            break

        matrice, elemento_attuale, finito = su(matrice, elemento_attuale)
        if finito:
            break

    return matrice


def is_matrice(matrice):
    if matrice == genera_matrice(len(matrice)):
        return True
    else:
        return False


# main

m1 = [
    [1]
]

m2 = [
    [1, 2],
    [4, 3]
]

m3 = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5],
]

m4 = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]

m5 = [
    [1, 2, 3, 4, 5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9],
]

no = [
    [1, 2, 3],
    [4, 5, 6]
]

no2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

no3 = [
    [3, 4],
    [2, 1]
]

print(is_matrice(m1))
print(is_matrice(m2))
print(is_matrice(m3))
print(is_matrice(m4))
print(is_matrice(m5))
print(is_matrice(no))
