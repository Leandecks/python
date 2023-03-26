# Leandro Gridelli




'''
Il seguente programma genera un codice unico identificativo "studente" usando questo processo:
- prime 2 lettere del nome
- prime 2 lettere del cognome
- classe elevata alla seconda e sezione
- indirizzo scritto al contrario saltando di 2 in 2
- radice quadrata del numero delle lettere della scuola. Questo nr è arrotondato a una sola cifra
- il codice finale è scritto in MAIUSCOLO

Esempio:
Input: Leandro, Gridelli, 1, e, Liceo, Marie Curie
Output: LEGR1EOCL3
'''




import math

nome=input("Inserisci il tuo nome: ")
cognome=input("Inserisci il tuo cognome: ")
classe=input("Inserisci la tua classe: ")
sezione=input("Inserisci la tua sezione: ")
indirizzo=input("Inserisci il tuo indirizzo scolastico (Liceo, tecnico, professionale): ")
scuola=input("Inserisci il nome della tua scuola: ")

classe=int(classe)
sqrtScuola=math.sqrt(len(scuola))
scuolaRounded=round(sqrtScuola)

codiceStudente=nome[:2]+cognome[:2]+str(classe**2)+sezione+indirizzo[::-2]+str(scuolaRounded)

print("Il tuo codice studente è:",codiceStudente.upper())
