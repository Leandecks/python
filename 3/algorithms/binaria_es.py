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

def cercas(lista, cercato):
    for el in lista:
        if el == cercato:
            return True
        elif el > cercato:
            return False
    return False

def cercab(lista, cercato):
    indexes = []
    index = len(lista) // 2
    
    while index not in indexes:
        print(index)
        if lista[index] == cercato:
            return True
        elif lista[index] > cercato:
            indexes.append(index)
            index //= 2
        else:
            indexes.append(index)
            index = index + index // 2
        
    return False
        
# main

lista = genero(100, 2, True, False, True)
print(cercas(lista, "ab"))
print(cercab(lista, "ab"))
