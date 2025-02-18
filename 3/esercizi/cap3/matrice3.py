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
        for j in range(colonne - 1):
            punti = random.randint(0, 30)
            r.append(punti)
                
        m.append(r)
        
    return m

def print_matrice(m):
    for k in m:
        for i in k:
            print(i, end = "\t")
        print()

# main

matrice = genera_matrice()
print(matrice)
print_matrice(matrice)

# nr, media
