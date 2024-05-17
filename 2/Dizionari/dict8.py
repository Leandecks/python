# Leandro Gridelli

import random

def totale(diz):
    return sum(list(diz.values()))

def media(diz):
    return sum(list(diz.values())) // len(diz) if len(diz) != 0 else False

def massimo(diz):
    m = list(diz.values())[0]
    piu_km = ""
    
    for k in diz:
        if diz[k] > m:
            m = diz[k]
            piu_km = k
            
    return piu_km

def minimo(diz):
    m = list(diz.values())[0]
    meno_km = ""
    
    for k in diz:
        if diz[k] < m:
            m = diz[k]
            meno_km = k
            
    return meno_km

def il_range(diz):
    return max(list(diz.values())) - min(list(diz.values()))

def randomico(diz):
    file = open("nomi.txt", encoding="utf-8")
    nomi = file.readlines()
    
    len_rand = random.randint(3, 10)
    nome_rand = nomi[random.randint(0, 9118)].strip("\n").capitalize()
    km_rand = random.randint(0, 10000)
    
    for k in range(len_rand):
        nome_rand = nomi[random.randint(0, 9118)].strip("\n").capitalize()
        km_rand = random.randint(0, 10000)
        diz[nome_rand] = km_rand
        
    file.close()
        
    return diz
    
# main

km = {}
print(randomico(km))


print(f"\nI km totali sono: {totale(km)}")
print(f"La media dei km è: {media(km)}")
print(f"Il più veloce è: {massimo(km)}")
print(f"Il più lento è: {minimo(km)}")
print(f"Il range è: {il_range(km)}")