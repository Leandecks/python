# Leandro Gridelli

'''
Date due liste in input, una di parole e una di numeri crea una nuova lista che contiene tutte
le combinazioni lettera-numero.
Il programma controlla che il prodotto delle lunghezze delle prime 2 liste sia uguale alle lunghezza
della terza lista.
Di questa terza lista verranno eliminati gli elementi primo e penultimo
es.
numeri = [1,2,3]
parole = [cane,gatto]
risultato = [1cane,1gatto,2cane,2gatto,3cane,3gatto]
2 * 3 = 6
finale = [1gatto,2cane,2gatto,3gatto]
'''

# Input delle liste

numeri = []
parole = []

while True:
  inserimento = input("Inserisci un numero: ")
  if inserimento == "q":
    break
  numeri.append(int(inserimento))


while True:
  inserimento = input("Inserisci una parola: ")
  if inserimento == "q":
    break
  parole.append(inserimento)

print(numeri, parole)

# Creazione della terza lista

terza = []

for i in numeri:
  for j in parole:
    terza.append(str(i) + j)

# Controllo della creazione

if len(numeri) * len(parole) == len(terza):
  print("La creazione della terza lista ha funzionato")
else:
  print("C'è stato un errore nella creazione della terza lista")

# Elimina degli elementi

del terza[0]
del terza[-2]

print(terza)