# Leandro Gridelli
import random

nc = 0
n = 0
while True:
    d1 = random.randint(0, 5) + 1
    d2 = random.randint(0, 5) + 1
    n = n + 1
    if d1 == d2:
        pass
    else:
        nc = nc + 1
    if d1 == 6 and d2 == 6:
        print(nc, n)
        break
