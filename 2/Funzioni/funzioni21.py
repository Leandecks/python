# Leandro Gridelli

import math


def is_triangolo(triangolo):

    """
    (list) -> Optional[float, bool]

    Restituisce l'area del triangolo se il parametro fornito è un triangolo.
    Se no restituisce False.

    >>> is_triangolo([3, 4, 5])
    6.0
    >>> is_triangolo([100, 1, 1])
    False
    """

    a, b, c = sorted(triangolo)
    p = (a + b + c) / 2

    if a + b > c:
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    else:
        return False


# main

lati = []

for k in range(3):
    lati.append(int(input("Inserisci un lato: ")))


print(is_triangolo(lati))
