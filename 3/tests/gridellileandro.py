# Leandro Gridelli

'''
Gioco: la bomba

In questo gioco possono giocare solo 2 o più giocatori.
Il programma fa inserire il nome ad ogni giocatore.
Ogni giocatore deve scrivere una parola contenente la sillaba data dal gioco.
La parola deve essere presente nel file delle parole della
lingua italiana. La sillaba deve essere composta da 2 lettere: 1 CONSONANTE + 1 VOCALE oppure
1 VOCALE + 1 CONSONANTE. La sillaba sarà generata a caso ogni nuovo turno.
La partita dura 3 turni.
In ogni turno il giocatore a cui tocca deve scrivere una parola valida contenente la sillaba.
Se risponde correttamente riceve un punto. Chi ha più punti vince

ESEMPIO DI OUTPUT:

Quanti giocatori sono presenti? 2
Giocatore 1, inserisci il tuo nome: leo
Giocatore 2, inserisci il tuo nome: enea

TURNO 1!
Tocca a leo:
Trova una parola con "YA"
Parola: yard
Risposta corretta!
Vinci un punto

Tocca a enea:
Trova una parola con "OG"
Parola: 
Hai sbagliato!
Vinci un punto

TURNO 2!
Tocca a leo:
Trova una parola con "ZO"
Parola: 
Hai sbagliato!
Vinci un punto

Tocca a enea:
Trova una parola con "HU"
Parola: 
Hai sbagliato!
Vinci un punto

TURNO 3!
Tocca a leo:
Trova una parola con "XA"
Parola: 
Hai sbagliato!
Vinci un punto

Tocca a enea:
Trova una parola con "AJ"
Parola: 
Hai sbagliato!
Vinci un punto

Ha vinto leo

'''

import random

def sillaba_random():
    vocali = "aeiou"
    consonanti = "bcdfghjklmnpqrstvwxyz"
    sillaba = ""
    
    voc_random = vocali[random.randint(0, 4)]
    con_random = consonanti[random.randint(0, 20)]
    
    caso = random.randint(0, 1)
    
    if caso == 0:
        sillaba += voc_random + con_random
    else:
        sillaba += con_random + voc_random
        
    return sillaba

def controlla(parola, sillaba):
    if sillaba not in parola:
        return False
    
    file = open("parole.txt")
    validato = False
    
    for ita in file:
        ita = ita.strip("\n")
        
        if parola == ita:
            validato = True
            
    file.close()
            
    return validato

def formatta_bool(b):
    if b == True:
        return "Risposta corretta!"
    else:
        return "Hai sbagliato!"
        
# main

giocatori = 0
nomi = []
punti = {}

while giocatori < 2:
    giocatori = int(input("Quanti giocatori sono presenti? "))
    
for j in range(1, giocatori + 1):
    nome = input(f"Giocatore {j}, inserisci il tuo nome: ")
    nomi.append(nome)
    
print()
    
for k in range(1, 4):
    print(f"TURNO {k}!")
    for gioc in nomi:
        print(f"Tocca a {gioc}:")
        sillaba = sillaba_random().upper()
        print(f'Trova una parola con "{sillaba}"')
        soluzione = input("Parola: ")
        correzione = controlla(soluzione, sillaba.lower())
        print(formatta_bool(correzione))
        print("Vinci un punto\n")
        if correzione:
            if gioc not in punti:
                punti[gioc] = 1
            else:
                punti[gioc] += 1
                
maxi = 0

for g in punti:
    if punti[g] > maxi:
        maxi= punti[g]
        mass = g

print("Ha vinto", g)
