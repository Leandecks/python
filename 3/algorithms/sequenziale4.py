# Leandro Gridelli

"""
Lista ordinata con elementi che possono essere ripetuti.
"""

def cerca(lista, cercato):
    c = 0

    for el in lista:
        if el == cercato:
            c += 1
        if c > 1 and el != cercato:
            return "fuck"
    return c

# main

print(cerca([1, 2, 2, 2, 3, 4], 2))
