# Leandro Gridelli

pesi = ["banane-4kg\n","mele-2kg\n","susine-3kg\n","arance-5kg\n","ananas-3kg\n"]
prezzi = ["banane-2€\n","susine-3€\n","arance-5€\n","ananas-3€\n","mele-2€\n"]

file_pesi = open("pesi.txt","w")
file_prezzi = open("prezzi.txt","w")

for peso in pesi:
   file_pesi.write(peso)

for prezzo in prezzi:
   file_prezzi.write(prezzo)

print("Dati scritti")
file_pesi.close()
file_prezzi.close()
