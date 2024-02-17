# Gridelli Leandro ML16 2EL 11/11/2023

lista = []
vocali_pari = []
cons_dispari = []

vocali = "aeiou"
consonanti = "bcdfghjklmnpqrstvwxyz"

nr_voc = 0
nr_cons = 0

lunga = []
corta = []
risultato = ""

while True:
   inserimento = input("Immetti parola, q per terminare. >>")
   if inserimento == "q":
      break
   lista.append(inserimento)

for parola in lista:
   for lettera in parola:
      if lettera in vocali:
         nr_voc += 1
      if lettera in consonanti:
         nr_cons += 1

   if nr_voc%2 == 0:
      vocali_pari.append(parola)
   if nr_cons%2 != 0:
      cons_dispari.append(parola)

   nr_voc = 0
   nr_cons = 0

vocali_pari.sort()
cons_dispari.sort()

if len(vocali_pari) > len(cons_dispari):
   lunga = vocali_pari
   corta = cons_dispari
else:
   lunga = cons_dispari
   corta = vocali_pari

for k in range(len(corta)):
   risultato += vocali_pari[k][0]
   risultato += cons_dispari[k][0]

print(f"\nLista parole immesse: {lista}\n")
print(f"Lista parole con un numero pari di vocali: {vocali_pari}")
print(f"Lista parole con un numero dispari di consonanti: {cons_dispari}")
print(f"\nrisultato = {risultato}")
