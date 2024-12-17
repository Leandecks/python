# Leandro Gridelli

import datetime

giorno = int(input("Inserisci la il giorno di nascita: "))
mese = int(input("Inserisci il numero del mese di nascita: "))
anno = int(input("Inserisci l'anno di nascita: "))

nascita = datetime.datetime(anno, mese, giorno)
oggi = datetime.datetime.today()
print(oggi - nascita)
