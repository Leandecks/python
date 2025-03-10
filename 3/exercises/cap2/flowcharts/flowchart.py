# Leandro Gridelli

import math

while True:
    a = input("Immetti a: ")
    if a != 0:
        break

b = int(input("Immetti b: "))
c = int(input("Immetti c: "))
d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(x1, x2)
else:
    if d == 0:
        print("Radici immaginarie")
    else:
        x = -b / (2 * a)
        print(x)
