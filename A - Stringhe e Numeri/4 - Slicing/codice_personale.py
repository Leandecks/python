# Leandro Gridelli

print("Immettere i seguenti dati:")
nome=input("Nome: ")
cognome=input("Cognome: ")
anno_nascita=int(input("Anno di nascita: "))
giorno_nascita=int(input("Giorno di nascita: "))
luogo_nascita=input("Luogo di nascita: ")

codice_minuscolo=nome[:3]+cognome[-3:]+str(anno_nascita//giorno_nascita)+luogo_nascita[:-4:-1]+str(anno_nascita%giorno_nascita)
codice_maiuscolo=codice_minuscolo.upper()
print("Il tuo codice personale è",codice_maiuscolo)
