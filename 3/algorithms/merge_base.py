# Leandro Gridelli

import random

def genera_stringa(k):
    stringa = ""
    lettere = "abcdefghilmnopqrstuvz"
    for j in range(k):
        stringa += lettere[random.randint(0, 20)]
    return stringa
    

def genero(n, k, ordine, ripetizione, stampa):
    lista = []
    
    for i in range(n):
        stringa = genera_stringa(k)
        if not ripetizione:
            while stringa in lista:
                stringa = genera_stringa(k)
                
        lista.append(stringa)
    
    if stampa:
        if ordine:
            print(sorted(lista))
        else:
            print(lista)
    
    if ordine:
        return sorted(lista)
    
    return lista

def merge(lista1, lista2):
    finale = []
    
    while True:
        if len(lista1) == 0 or len(lista2) == 0:
            break
        elif lista1[0] > lista2[0]:
            finale.append(lista2[0])
            del lista2[0]
        elif lista1[0] == lista2[0]:
            finale.append(lista1[0])
            del lista1[0]
            del lista2[0]
        else:
            finale.append(lista1[0])
            del lista1[0]
            
    if len(lista1) > 0:
        finale.extend(lista1)
    elif len(lista2) > 0:
        finale.extend(lista2)
    
    return finale      

# main

l1 = genero(10, 1, True, False, True)
l2 = genero(10, 1, True, False, True)

print(merge(l1, l2))
