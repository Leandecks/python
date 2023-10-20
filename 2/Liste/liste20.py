# Leandro Gridelli

a = []
elemento = ""
identiche = []

while True:
   elemento = input("Inserisci un elemento: ")
   if elemento == "q":
      break
   if elemento not in a:
      a.append(elemento)

for k in a:
   for i in k:
      if i in k:
         identiche.append(k)

print(a)
