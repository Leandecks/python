# Leandro Gridelli

import math


def is_triangolo(triangolo):

    a, b, c = sorted(triangolo)
    p = (a + b + c) / 2

    if a + b > c:
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    else:
        return False


# main

print(is_triangolo([4, 3, 5]))
