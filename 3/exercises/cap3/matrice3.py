# Leandro Gridelli

import random

def genera_matrice():
    righe = int(input("Inserisci i giocatori: "))
    colonne = int(input("Inserisci le volte di punti da inserire: "))
    
    m = []
    
    for k in range(righe):
        r = []
        numero = random.randint(1, 99)
        r.append(numero)
        for j in range(colonne):
            punti = random.randint(0, 30)
            r.append(punti)
                
        m.append(r)
        
    return m

def print_matrice(m):
    for k in m:
        for i in k:
            print(i, end = "\t")
        print()

def trova_moda(lista):
    d = {}

    for el in lista:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1

    mass = 0

    for k in d:
        if d[k] > mass:
            mass = d[k]
            massimo = k

    if list(d.values()).count(mass) > 1:
        return -1

    return massimo

def trova_mediana(lista):
    lista = sorted(lista)

    if len(lista) % 2 == 0:
        return (lista[len(lista) // 2] + lista[(len(lista) // 2) - 1]) / 2
    else:
        return lista[len(lista) // 2]

def genera_matrice2(mat):
    righe = len(mat)
    colonne = 4

    m = []

    for riga in mat:
        r = []
        r.append(riga[0])

        c = 0
        lista_punti = []

        for colonna in range(1, len(riga)):
            lista_punti.append(riga[colonna])

        media = round(sum(lista_punti) / len(lista_punti), 2)
        moda = trova_moda(lista_punti)
        mediana = trova_mediana(lista_punti)

        r.append(media)
        r.append(moda)
        r.append(mediana)

        m.append(r)

    return m

# main

matrice = genera_matrice()
print()
print_matrice(matrice)
print()

# nr, media, mediana, moda

matrice2 = genera_matrice2(matrice)
print_matrice(matrice2)
