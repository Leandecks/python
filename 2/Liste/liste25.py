# Leandro Gridelli

'''
Creare una lista di numeri e stampare la lista con i numeri invertiti.
'''

lista = []
invertita = []

while True:
   inserimento = input("Inserisci un numero: ")
   if inserimento == "q":
      break
   lista.append(int(inserimento))

for k in range(len(lista)-1, -1, -1):
   invertita.append(lista[k])

print(lista)
print(invertita)
