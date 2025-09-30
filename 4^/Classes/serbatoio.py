# Leandro Gridelli

def aggiungere(c, ci):
    aggiunta = int(input("Quantità da aggiungere: "))
    if c + aggiunta > ci:
        print("Valore troppo grande, annullato\n")
    else:
        c += aggiunta
        
    return c
        
def togliere(c):
    preleva = int(input("Quantità da prelevare: "))
        
    if c - preleva < 0:
        print("Valore troppo grande")
    else:
        c -= preleva
        
    return c

def riservare(c, r):
    if c < r:
        print("RISERVA: il serbatoio è quasi vuoto")
        
def vuotare():
    return 0

def riempire(ci):
    return ci

def init_serbatoio(nome):
    print(f"Sei nel serbatoio {nome.upper()}")
    capienza_ini = int(input("Inserire capienza: "))
    riserva = int(input("Inserire riserva: "))
    capienza = capienza_ini
    return nome, capienza, capienza_ini, riserva
        
def serbatoio(nome, capienza, capienza_ini, riserva):
    print(f"Sei nel serbatoio {nome.upper()}")
    while True:
        print(f"La capienza è {capienza}")
        
        riservare(capienza, riserva)
            
        azione = input("Scegli azione:\na - aggiungi\np - preleva\nv - vuota\nf - fai il pieno\nq - esci\n\n> ")
        
        if azione == "q":
            break
        elif azione == "a":
            capienza = aggiungere(capienza, capienza_ini)
        elif azione == "p":
            capienza = togliere(capienza)
        elif azione == "v":
            capienza = vuotare()
        elif azione == "f":
            capienza = riempire(capienza_ini)
            
    return nome, capienza, capienza_ini, riserva

def serbatoi():
    acquan, acquac, acquaci, acquar = init_serbatoio("acqua")
    benzan, benzac, benzaci, benzar = init_serbatoio("benzina")
    vinon, vinoc, vinoci, vinor = init_serbatoio("vino")

    while True:
        scelta = input("Scegli il serbatoio. 'a' per acqua, 'b' per benzina, 'v' per vino: ")
        if scelta == "a":
            acquan, acquac, acquaci, acquar = serbatoio(acquan, acquac, acquaci, acquar)
        elif scelta == "b":
            benzan, benzac, benzaci, benzar = serbatoio(benzan, benzac, benzaci, benzar)
        elif scelta == "v":
            vinon, vinoc, vinoci, vinor = serbatoio(vinon, vinoc, vinoci, vinor)
        else:
            continue
        
# main

serbatoi()
