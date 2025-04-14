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


def merge(a, b):
    a = a.copy()
    b = b.copy()
    
    finale = []
    tappo = 100
    a.append(tappo)
    b.append(tappo)
    
    for k in range(len(a) + len(b) - 1):
        if a[0] < b[0]:
            finale.append(a[0])
            del a[0]
        else:
            finale.append(b[0])
            del b[0]
            
    del finale[-1]
    return finale
    

# main

l1 = [0, 3, 5, 8]
l2 = [1, 2, 4, 7, 9]

print(l1, l2)
print(merge(l1, l2))
