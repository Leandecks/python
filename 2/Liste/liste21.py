# Leandro Gridelli

lista = []
duea = []
doppie = []

# inserimento

while True:
   inserimento = input("Inserisci una parola: ")
   if inserimento == "q":
      break
   lista.append(inserimento)

# cerca parole con 2 a

lista = ["cane","panna","bicicletta","banana","panno"]

numeroa = 0

for parola in lista:
   for lettera in parola:
      if lettera == "a":
         numeroa += 1
      if numeroa >= 2:
         duea.append(parola)
         numeroa = 0

# cerca parole con doppie

for parola in lista:
   for posizione_lettera in range(len(parola)):
      if parola[posizione_lettera] == parola[posizione_lettera+1]:
         doppie.append(k)

print(lista)
print(duea)
##print(doppie)
