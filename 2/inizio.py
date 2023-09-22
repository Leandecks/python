# Leandro Gridelli

'''
Lo script restituisce una parola randomica di modello cvcvcv... dove c è una consonante e v è una vocale.
Le lettere doppie sono troncate (variante: sostituite)
La lunghezza della parola è data da un numero in input forzato pari e non negativo
'''

import random

numero = int(input("Inserisci un numero: "))

if numero < 0:
   numero = (numero * -2) / 2
   

if numero%2==0:
   numero = numero
else:
   numero += 1

parola = ""

vocali = "aeiou"
consonanti = "bcdfglmnpqrstvxyz"

c_usate = ""
v_usate = ""

for k in range(int(numero/2)):
   c = consonanti[random.randint(0,16)]

   if c in c_usate:
      parola = parola
      c_usate = c_usate
   else:
      parola += c
      c_usate += c

   
   v = vocali[random.randint(0,4)]

   if v in v_usate:
      parola = parola
      v_usate = v_usate
   else:
      parola += v
      v_usate += v


print("La parola nuova è:", parola)
print("La parola potrebbe non essere perfetta dato che le lettere doppie sono troncate")
