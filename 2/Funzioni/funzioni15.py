# Leandro Gridelli

def dispari(lista, n):
    somma_dispari = 0
    for k in lista:
        if k % 2 != 0:
            somma_dispari += k

    return somma_dispari * n

# main

print(dispari([2,3,4,5],3))