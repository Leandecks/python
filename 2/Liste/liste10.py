# Leandro Gridelli

a = []
b = []
c = []

volte = int(input("Quanti numeri vuoi inserire? "))

for k in range(volte):
   inserta = int(input("Inserisci un numero: "))
   a.append(inserta)

volte = int(input("Quanti numeri vuoi inserire? "))

for k in range(volte):
   inserta = int(input("Inserisci un numero: "))
   b.append(inserta)

c += a[:2]
c += b[-4:]

print(a)
print(b)
print(c)
