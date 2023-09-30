# Leandro Gridelli

'''
Scrivi un programma che calcoli il massimo e il minimo di una serie di numeri inseriti da tastiera e,
se sia il massimo che il primo sono pari aggiunge 2 ad entrambi, altrimenti i numeri inseriti restano invariati
'''

import random
massimo = 0
primoNumero = 0

for k in range(random.randint(1,10)):
   numero = int(input("Inserisci un numero: "))
   if numero > massimo:
      massimo = numero
   if k == 1:
      primoNumero = k

if massimo%2==0 and primoNumero%2==0:
   massimo += 2
   primoNumero += 2

print("Il numero più alto è (se pari è di 2 più alto):",massimo)
print("Il primo numeri inserito è (se pari è di 2 più alto):",primoNumero)
