# Leandro Gridelli

file_pesi = open("pesi.txt")
file_prezzi = open("prezzi.txt")

pesi = []
for riga in file_pesi:
   pesi.append(riga.split("-"))
   
prezzi = []
for riga in file_prezzi:
   prezzi.append(riga.split("-"))

prezzo_totale = 0

for peso in pesi:
   for prezzo in prezzi:
      if peso[0] in prezzo[0]:
         peso[1] = peso[1].strip("\n")
         print(f"Il prodotto {peso[0]} pesa {peso[1]}")
         print(f"Il prodotto {prezzo[0]} pesa {prezzo[1]}")
         prezzo_totale += int(prezzo[1].strip("€\n"))

print(f"In totale spendi: {prezzo_totale}€")
