# Leandro Gridelli

"""
Lista ordinata e composta da elementi distinti.
"""

def cerca(lista, cercato):
    for el in lista:
        if el == cercato:
            return True
        elif el > cercato:
            return False
    return False

# main

print(cerca([1, 2, 4], 0))
