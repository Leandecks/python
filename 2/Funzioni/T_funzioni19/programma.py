# Leandro Gridelli

import func
# from funz import * ### Male => la seconda funzione di quadrato sovrascrive la prima
import func2 as f

# main

a = int(input("Primo numero: "))
b = int(input("Secondo numero: "))

print(func.cubo(a))
print(func.quadrato(b))
print(func.area(a, b))

print(f.triangolo(a, b))
print(f.quadrato(b))

print(help(func.quadrato))
