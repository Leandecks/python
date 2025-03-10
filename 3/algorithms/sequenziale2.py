# Leandro Gridelli

"""
Lista non ordinata con elementi che possono essere ripetuti.
"""

def cerca(lista, cercato):
    c = 0

    for el in lista:
        if el == cercato:
            c += 1

    return c

# main

print(cerca([1, 2, 3, 4, 3], 3))
