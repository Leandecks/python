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

def bubble(lista):
    c = 0
    
    while True:
        for i in range(len(lista)):
            c += 1
            print(c, len(lista))
            if c > len(lista):
                return lista
            if not i == len(lista) - 1:
                if lista[i] > lista[i + 1]:
                    c = 0
                    scambio = lista[i]
                    lista[i] = lista[i + 1]
                    lista[i + 1] = scambio

# main

l = genero(10, 2, False, False, True)
print(bubble(l))
