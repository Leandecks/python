# Leandro Gridelli

'''
Il programma deve generare il seguente quiz di matematica:
- La prima domanda chiederà il risultato di una potenza di base [0-10] ed esponente [0-3]
- La seconda domanda chiederà il risultato della radice quadrata di 64
- La terza domanda chiederà il risultato di una sottrazione tra [500-1000] e [0-500]
- La quarta domanda chiederà se il numero [0-1000] è divisibile per 3
Infine il codice darà un voto:
- 10 se le risposte corrette sono 4/4
- 8 se le risposte corrette sono 3/4
- 6 se sono 2/4
- 4 se è 1/4
- 2 se è 0/4
Se richiesti, dai tutti i risultati dettagliati
'''

# IMPORT

import random
import math

# VARIABILI RANDOM PER DOMANDE

base = random.randint(0,10)
esponente = random.randint(0,3)

sottraendo = random.randint(500,1000)
minuendo = random.randint(0,500)

numero = random.randint(0,1000)

# QUIZ

uno = int(input(f"Quanto fa {base}^{esponente}? "))
due = int(input(f"Qual'è la radice quadrata di 64? "))
tre = int(input(f"Quanto fa {sottraendo}-{minuendo}? "))
quattro = input(f"{numero} è divisibile per 3? (True/False) ")

# BOOLEAN PER CONTROLLO SE RISPOSTA È CORRETTA

if uno == (base**esponente):
    uno_corretta = True
else:
    uno_corretta = False
if due == 8:
    due_corretta = True
else:
    due_corretta = False
if tre == (sottraendo-minuendo):
    tre_corretta = True
else:
    tre_corretta = False
if (quattro == "True" and numero % 3 == 0) or (quattro == "False" and numero % 3 != 0):
    quattro_corretta = True
else:
    quattro_corretta = False

# RISULTATI

dett = input("Vuoi dei risultati dettagliati? (SI/NO) ").upper()
print("\n\n")

if dett == "SI":
    print(f"Domanda 1: {uno_corretta}")
    print(f"Domanda 2: {due_corretta}")
    print(f"Domanda 3: {tre_corretta}")
    print(f"Domanda 4: {quattro_corretta}\n\n")

    if uno_corretta and due_corretta and tre_corretta and quattro_corretta:
        print("VOTO: 10\n")
    elif (uno_corretta and due_corretta and tre_corretta) or (uno_corretta and due_corretta and quattro_corretta) or (uno_corretta and tre_corretta and quattro_corretta) or (due_corretta and tre_corretta and quattro_corretta):
        print("VOTO: 8\n")
    elif (uno_corretta and due_corretta) or (uno_corretta and tre_corretta) or (uno_corretta and quattro_corretta) or (due_corretta and tre_corretta) or (due_corretta and quattro_corretta) or (tre_corretta and quattro_corretta):
        print("VOTO: 6\n")
    elif uno_corretta or due_corretta or tre_corretta or quattro_corretta:
        print("VOTO: 4\n")
    else:
        print("VOTO: 2\n\n")
    print(f"DOMANDA 1: Quanto fa {base}^{esponente}? ")
    print(f"RISPOSTA: {uno}; RISPOSTA CORRETTA: {base**esponente}\n")
    print(f"DOMANDA 2: Qual'è la radice quadrata di 64? ")
    print(f"RISPOSTA: {due}; RISPOSTA CORRETTA: 8\n")
    print(f"DOMANDA 3: Quanto fa {sottraendo}-{minuendo}? ")
    print(f"RISPOSTA: {tre}; RISPOSTA CORRETTA: {sottraendo-minuendo}\n")
    print(f"DOMANDA 4: {numero} è divisibile per 3? (True/False)")
    print(f"RISPOSTA: {quattro}; RISPOSTA CORRETTA: {(quattro and numero % 3 == 0) or (not quattro and numero % 3 != 0)}")

elif dett == "NO":
    print(f"Domanda 1: {uno_corretta}")
    print(f"Domanda 2: {due_corretta}")
    print(f"Domanda 3: {tre_corretta}")
    print(f"Domanda 4: {quattro_corretta}\n\n")

    if uno_corretta and due_corretta and tre_corretta and quattro_corretta:
        print("VOTO: 10\n\n")
    elif (uno_corretta and due_corretta and tre_corretta) or (uno_corretta and due_corretta and quattro_corretta) or (uno_corretta and tre_corretta and quattro_corretta) or (due_corretta and tre_corretta and quattro_corretta):
        print("VOTO: 8\n\n")
    elif (uno_corretta and due_corretta) or (uno_corretta and tre_corretta) or (uno_corretta and quattro_corretta) or (due_corretta and tre_corretta) or (due_corretta and quattro_corretta) or (tre_corretta and quattro_corretta):
        print("VOTO: 6\n\n")
    elif uno_corretta or due_corretta or tre_corretta or quattro_corretta:
        print("VOTO: 4\n\n")
    else:
        print("VOTO: 2\n\n")
else:
    print("Non è né un si né un no")