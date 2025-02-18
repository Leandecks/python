# Leandro Gridelli

import random

def matrice():
    righe = int(input("Righe: "))
    colonne = int(input("Colonne: "))
    
    m = []
    
    for ri in range(righe):
        r = []
        for c in range(colonne):
            r.append(random.randint(1, 100))
        m.append(r)
        
    return m

def stampa(m):
    for r in m:
        for c in r:
            print(c, end="\t")
        print()
        
def massimo(m):
    mass = m[0][0]
    
    for r in m:
        for c in r:
            if c > mass:
                mass = c
    
    return mass

def minimo(m):
    mini = m[0][0]
    
    for r in m:
        for c in r:
            if c < mini:
                mini = c
    
    return mini

def somma(m):
    s = 0
    
    for r in m:
        for c in r:
            s += c
            
    return s

# main

matrice = matrice()
print()
stampa(matrice)
print()
print("Massimo:", massimo(matrice))
print("Minimo:", minimo(matrice))
print("Somma:", somma(matrice))
