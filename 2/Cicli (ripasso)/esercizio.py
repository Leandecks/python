# Leandro Gridelli

'''
L'utente può scegliere quante volte inserire una lettera dell'alfabeto.
Il programma convertirà la lettera in un numero rappresentante la posizione della lettera nell'alfabeto.
Tutti i numeri generati dalle lettere saranno concatenati in un numero solo.
Infine viene controllato se il numero è divisibile per dei numeri casuali (compresi fra 1 e 10) minori di esso.
La quantità di questi numeri è data dal numero inserito inizialmente.
'''

import random

volte = int(input("Quante lettere vuoi inserire? "))

lettereUsate = ''
numero = ''
alfabeto = "abcdefghijklmnopqrstuvwxyz"

for k in range(volte):
  lettera = input("Inserisci una lettera dell'alfabeto: ")
  lettereUsate += lettera

for let in lettereUsate:
  index = alfabeto.find(let)
  numero += str(index)

for i in range(volte):
  rand = random.randint(1,10)
  if int(numero) % rand == 0:
    print(f"{numero} è divisibile per {rand}")
  else:
    print(f"{numero} non è divisibile per {rand}")
