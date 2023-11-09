# Leandro Gridelli

'''
Scrivi un programma che chiede all'utente di inserire una lista di numeri e stampa la lista con i numeri che sono divisibili per un certo numero.
'''

lista = []
divisibili = []
numero = int(input("Inserisci il numero per il quale vuoi controllare la divisibilità: "))

while True:
   inserimento = input("Inserisci un numero: ")
   if inserimento == "q":
      break
   lista.append(int(inserimento))

for k in lista:
   if k%numero == 0:
      divisibili.append(k)

print(lista)
print(divisibili)
