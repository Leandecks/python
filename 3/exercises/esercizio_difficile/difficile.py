# Leandro Gridelli

def is_spirale(m):
##    if m[0][0] != 1:
##        return False

    # prima riga

    lato = len(m[0])

    m0 = []

    for k in range(lato):
        m0.append(k + 1)

    if m[0] != m0:
        return False

    # ultima colonna

    ultima_colonna = []

    for r in m:
        ultima_colonna.append(r[lato - 1])

    contatore = 0

    for j in m:
        if j[lato - 1] != ultima_colonna[contatore]:
            return False
            
        contatore += 1

    print(ultima_colonna)

    # seconda riga

    if m[1][-1] != lato + 1:
        return False

    ordine = []
    c = 0

    for riga in m:
        if c == 0:
            ordine.extend(m[c])
        c += 1

    print(ordine)
    

# main

m = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5],
]

is_spirale(m)

