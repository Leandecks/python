# Leandro Gridelli

a = []
b = []

volte = int(input("Quanti numeri vuoi inserire? "))

for k in range(volte):
   inserta = int(input("Inserisci un numero: "))
   a.append(inserta)

volte = int(input("Quanti numeri vuoi inserire? "))

for k in range(volte):
   inserta = int(input("Inserisci un numero: "))
   b.append(inserta)

print(a)
print(b)
print("Elementi solo presenti in a:")

for k in a:
   if k not in b:
      print(k)
