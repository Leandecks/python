# Leandro Gridelli 3EL ML07

import random

def genera_diz(lista):
    diz = {}
    for k in lista:
        temp1 = 1
        temp2 = 0
        while temp1 > temp2:
            temp1 = random.randint(-2, 8)
            temp2 = random.randint(-2, 8)
        tup = (temp1, temp2)
        diz[k] = tup
    return diz
        
def t_min(diz):
    mini = 9
    cit = []
    for key in diz:
        if diz[key][0] <= mini:
            if diz[key][0] == mini:
                cit.append(key)
            else:
                mini = diz[key][0]
                citta = key
    cit.append(citta)
  
    return cit, mini

def t_max(diz):
    maxi = -3
    cit = []
    for key in diz:
        if diz[key][1] >= maxi:
            if diz[key][0] == maxi:
                cit.append(key)
            else:
                maxi = diz[key][1]
                citta = key
    cit.append(citta)
    return cit, maxi

def ghiaccio(diz):
    g = set()
    for key in diz:
        if diz[key][0] < 0:
            g.add(key)
    return g

def caldo(diz):
    c = set()
    for key in diz:
        if diz[key][0] > 3:
            c.add(key)
    return c

def gelo(diz):
    g = set()
    for key in diz:
        if diz[key][0] < 2 and diz[key][1] < 2:
            g.add(key)
    return g

def escursione(diz):
    esc = []
    for key in diz:
        esc.append((diz[key][1] - diz[key][0], key))
    return esc

def print_diz(diz):
    for k in diz:
        print(f"capitale:\t{k}\t temperatura minime:\t{diz[k][0]}\t temperatura massima:\t{diz[k][1]}\t")
        
def print_esc(e):
    for escu in e:
        print(f"Capitale :  {escu[1]} 	 escursione termica: {escu[0]}")
        
def esc_10(e):
    lis = []
    for escu in e:
        if escu[0] == 10:
            lis.append(escu[1])
    if len(lis) > 0:
        return lis
    else:
        return "Nessuna"

#  main

capitali=['Roma','Parigi','Madrid','Londra','Berlino','Mosca','Atene','Praga','Dublino','Oslo']

dizio = genera_diz(capitali)
temp_min = t_min(dizio)
temp_max = t_max(dizio)
ghiaccio = ghiaccio(dizio)
caldo = caldo(dizio)
gelo = gelo(dizio)
esc_termica = escursione(dizio)

# output

print("1) il Dizionario :")
print_diz(dizio)
print("\n2) Le capitali con la temperatura minima più bassa sono :")
print(f"\t{temp_min[0]}\tdove ci sono {temp_min[1]} gradi")
print("\n3) Le capitali con la temperatura massima più alta sono :")
print(f"\t{temp_max[0]}\tdove ci sono {temp_max[1]} gradi")
print("\n4) Set Giaccio - capitali con temperatura minima sotto lo zero :")
print(ghiaccio)
print("\n5) Set Caldo - capitali con temperatura minima superiore a 3 gradi :")
print(caldo)
print("\n6) Set Gelo - capitali con temperatura minima e massima inferiore ai 2 gradi :")
print(gelo)
print("\n7) Lista delle escursioni termiche in ordine crescente:")
print_esc(esc_termica)
print(f"\n8) Capitali con escursione uguale a 10:  {esc_10(esc_termica)}")
