# Leandro Gridelli

'''
Scrivi un programma che chiede all'utente di inserire una lista di numeri e stampa la lista con i numeri che sono numeri perfetti.
Esempi:
6: divisori sono 1,2,3: 1+2+3 = 6
28...
'''

lista = []
perfetti = []

while True:
   numero = input("Inserisci un numero: ")
   if numero == "q":
      break
   lista.append(int(numero))

for k in lista:
   # Scomposizione in fattori primi
   
print(lista)
print(perfetti)
