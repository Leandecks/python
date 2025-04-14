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

def selection(lista):
    occupati = 0
    
    for k in range(len(lista)):
        mini = lista[occupati]
        for elemento in lista[occupati:]:
            if elemento < mini:
                mini = elemento
            
        scambio = lista[0 + occupati]
        lista[lista.index(mini)] = scambio
        lista[0 + occupati] = mini
    
        occupati += 1
        
    return lista

# main

l = genero(10, 2, False, False, True)
print(selection(l))
