# Leandro Gridelli

import random

file = open("cod11.txt", "w")

for k in range(10):
    b = ""

    for l in range(7):
        b += str(random.randint(0, 1))

    if b.count("1") % 2 == 0:
        file.write("0" + b + "\n")
    else:
        file.write("1" + b + "\n")

file.close()
