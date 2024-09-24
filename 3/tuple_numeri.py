# Leandro Gridelli

import random

def genera_tuple():
    lista = []
    
    for k in range(13):
        lunghezza = random.randint(2, 20)
        tupla = ()
        
        for i in range(lunghezza):
            numero = random.randint(1, 10)
            tupla = tupla + (numero,)
        
        lista.append(tupla)
        
    return lista

def media(t):
    return round((sum(t) / len(t)), 2)

def genera_diz(lista):
    diz = {}
    
    for t in lista:
        diz[t] = media(t)
        
    return diz
        
# main

lista_tuple = genera_tuple()
print(f"Lista ottenuta: {lista_tuple}\n\n")

for tup in range(len(lista_tuple)):
    print(f"Tupla nr {tup}")
    print(f"Lunghezza tupla: {len(lista_tuple[tup])}")
    print(f"Media tupla: {media(lista_tuple[tup])}")
    print(f"Contenuto: {lista_tuple[tup]}\n")
    
print(f"Dizionario: {genera_diz(lista_tuple)}")
