# Leandro Gridelli

'''
Lo script restituisce una parola randomica di modello cvcvcv... dove c è una consonante e v è una vocale.
Le lettere doppie sono sostituite
La lunghezza della parola è data da un numero in input forzato pari e non negativo
'''

import random

numero = int(input("Inserisci un numero: "))

if numero < 0:
    numero = (numero * -2) / 2

if numero % 2 == 0:
    numero = numero
else:
    numero += 1

parola = ""

vocali = "aeiou"
consonanti = "bcdfglmnpqrstvxyz"

c_usate = ""
v_usate = ""

i = 0
u = 0

for k in range(numero // 2):
    c = consonanti[random.randint(0, 16)]

    while c in c_usate:
        c = consonanti[random.randint(0, 16)]
        i += 1
        if i > 30:
            break

    if i > 30:
        break

    c_usate += c
    parola += c

    #######################################

    v = vocali[random.randint(0, 4)]

    while v in v_usate:
        v = vocali[random.randint(0, 4)]
        i += 1
        if u > 30:
            break

    if u > 30:
        break

    v_usate += v
    parola += v

print("La parola nuova è:", parola)
print("La parola potrebbe non essere perfetta dato che le lettere doppie sono troncate")
