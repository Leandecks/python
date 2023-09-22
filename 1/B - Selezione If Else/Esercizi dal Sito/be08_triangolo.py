# Leandro Gridelli

lato1 = int(input("Lunghezza lato 1: "))
lato2 = int(input("Lunghezza lato 2: "))
lato3 = int(input("Lunghezza lato 3: "))

if lato1 == lato2 == lato3:
    tipo = "equilatero"
elif lato1 == lato2 or lato2 == lato3 or lato1 == lato3:
    tipo = "isoscele"
else:
    tipo = "scaleno"

print(f"Il triangolo è {tipo}")