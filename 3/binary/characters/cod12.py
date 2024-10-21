# Leandro Gridelli

import random

file = open("cod11.txt").read()

arr = []
for k in range(3):
    arr.append(random.randint(0, len(file)))

nuova = ""

for i in range(len(file)):
    if i in arr:
        if file[i] == "1":
            nuova += "0"
        else:
            nuova += "1"
    else:
        nuova += file[i]

file2 = open("cod12.txt", "w")
file2.write(nuova)
file2.close()
