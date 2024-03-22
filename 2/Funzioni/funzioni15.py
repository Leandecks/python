# Leandro Gridelli

def dispari(lista, n):
    somma_dispari = 0

    for k in lista:
        if k % 2 != 0:
            somma_dispari += k

    return somma_dispari * n

def posizioni(lista, n):
    somma = 0

    for k in range(len(lista)):
        if k % 2 != 0:
            somma += lista[k] // n

    return somma

# main

print(dispari([2,3,4,5],3))
print(posizioni([2,6,3,15,4], 3))