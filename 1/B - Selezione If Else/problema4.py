# Leandro Gridelli

'''
Calcolatrice Universale
Scelta l'operazione (+,*,-,/,^,radice,divisione intera,resto,
media matematica,errore relativo,errore relativo percentuale,semidispersione,percentuale
) calcola il risultato fra 2 numeri random 1-10, se necessario aggiungi altre variabili per i calcoli speciali

OUTPUT: Print diverso per matematica / fisica / percentuale
'''

# IMPORT

import random
import math

# SCELTA

scelta = input("Scegli che operazione vuoi eseguire:\nA [+]\nS [-]\nM [*]\nD [:]\nP [^]\nQ [radice]\nR [resto]\nI [divisione intera]\nME [Media]\nER [errore relativo]\nERP [errore relativo percentuale]\nEA [Semidispersione]\n% [percentuale]\nSCELTA: ")

# VARIABILI MATEMATICA

x = random.randint(1,10)
y = random.randint(1,10) # solo usato se necessario
perc = random.randint(1,100)

# VARIABILI FISICA

misura = random.randint(1,100)
errore = random.randint(0,10)
n_misure = random.randint(1,10)

ris = 0

# CALCOLO DI RIS

if scelta == "A":
    ris = x+y
elif scelta == "S":
    ris = x-y
elif scelta == "M":
    ris = x*y
elif scelta == "D":
    ris = x/y
elif scelta == "I":
    ris = x//y
elif scelta == "R":
    ris = x%y
elif scelta == "P":
    ris = x**y
elif scelta == "Q":
    ris = math.sqrt(x)
elif scelta == "ME":
    ris = (x+y)/2
elif scelta == "ER":
    ris = errore/misura
elif scelta == "ERP":
    ris = errore/misura*100
elif scelta == "EA":
    ris = (misura-errore) / n_misure
elif scelta == "%":
    ris = x * (perc/100)

# OUTPUT

print()

if scelta == "ER" or scelta == "ERP" or scelta == "EA":
    print(f"Misura: {misura}")
    print(f"Errore: {errore}")
    print(f"Risultato: {ris}")
elif scelta == "%":
    print(f"x: {x}")
    print(f"Percentuale: {perc}%")
    print(f"Risultato: {ris}&")
else:
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"Risultato: {ris}")