# Leandro Gridelli

import random

a = "abcdefghijklmnopqrstuvwxyz"
a = list(a)

print(f"a = {a}")

n = []

# modo mio
for k in range(4):
  ran = random.randint(0,25)
  while ran in n:
    ran = random.randint(0,25)
  n.append(ran)

# modo prof
##while True:
##  el = random.randint(0,26)
##  if el not in n:
##    n.append(el)
##  if len(n) == 4:
##    break

print(f"n = {n}")

for i in n:
  a[i] = ["VUOTO"]

print(f"a = {a}")
