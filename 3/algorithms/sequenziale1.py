# Leandro Gridelli

"""
Lista non ordinata e composta da elementi distinti.
"""

def cerca(lista, cercato):
    for el in lista:
        if el == cercato:
            return True
    return False

# main

print(cerca([1, 2, 3, 4], 0))
