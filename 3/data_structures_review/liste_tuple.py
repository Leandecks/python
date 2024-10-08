# Leandro Gridelli

import random

def lista1():
    lista = []
    for k in range(5):
        lista.append(random.randint(1, 9))
    return lista

def lista2():
    lista = []
    for k in range(5):
        lista.append(random.randint(10, 99))
    return lista

def ordina(l1, l2):
    l1 = sorted(l1)
    l2 = sorted(l2)
    
    finale = set()
    
    for k in range(5):
        tup = (l1[k], l2[k])
        finale.add(tup)
        
    return finale

def prodotto_maggiore(ordinate):
    mass = float("-inf")
    for coppia in ordinate:
        prodotto = coppia[0] * coppia[1]
        if prodotto > mass:
            mass = prodotto
    return mass

# main

lista1 = lista1()
lista2 = lista2()
print(f"n1 = {lista1}, n2 = {lista2}")
coppie = ordina(lista1, lista2)
print(f"Coppie ordinate: {coppie}")
print(f"Prodotto maggiore delle coppie: {prodotto_maggiore(coppie)}")
