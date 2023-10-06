# Leandro Gridelli

import random

a = "abcdefghijklmnopqrstuvwxyz"
a = list(a)

print(f"a = {a}")

n = []

for k in range(4):
  n.append(random.randint(0,26))

print(f"n = {n}")

for i in n:
  a[i] = ["VUOTO"]

print(f"a = {a}")