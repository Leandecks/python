# Leandro Gridelli

import random

# main

n = str(bin(random.randint(0, 1048576))).strip("0b")
if len(n) < 32:
    n = (32 - len(n)) * "0" + n
print(n[:16] + " " + n[16:])
