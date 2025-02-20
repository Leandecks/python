# Leandro Gridelli

def is_spirale2(m):

    """
    1. ->
    2. v
    3. <-
    4. ^
    """

    lista = []
    posizione = "0,0"
    lato = len(m)

    x = 0
    y = 0

    # ->

    for riga in m:
        for valore in riga:
            if f"{x},{y}" == posizione:
                lista.extend(riga[x:])
                # posizione = f"{}"

            y += 1

        x += 1

    print(lista)

    return m

def is_spirale(m):
    # ->

    lista = []

    for riga in m:
        lista.extend(riga)

    # print(lista)

def genera_matrice(lato):
    matrix = []

    # RIGA 1

    riga1 = []

    for a in range(1, lato + 1):
        riga1.append(a)

    matrix.append(riga1)

    # MATRICE 1*1

    if lato == 1:
        return matrix

    # RIGA 2

    riga2 = []
    ultimo_riga1 = riga1[-1]
    lunghezza_curva_per_riga2 = (lato - 1) * 2 + (lato - 2)
    primo_riga2 = ultimo_riga1 + lunghezza_curva_per_riga2
    ultimo_riga2 = ultimo_riga1 + 1

    for b in range(primo_riga2, primo_riga2 + (lato - 1)):
        riga2.append(b)

    riga2.append(ultimo_riga2)
    matrix.append(riga2)

    # MATRICE 2*2

    if lato == 2:
        return matrix

    # LATO 3

    riga3 = []
    primo_riga3 = primo_riga2 - 1
    ultimo_riga3 = ultimo_riga2 + 1

    # print(matrix)

# main

m1 = [
    [1]
]

m2 = [
    [1, 2],
    [4, 3]
]

matrice = [
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

is_spirale(matrice)
genera_matrice(4)
