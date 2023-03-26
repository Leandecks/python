# Leandro Gridelli

parola = input("Inserisci la tua parola con lunghezza multiplo di 3: ")


lunghezzaParteUno = len(parola) / 3 * 2

parteUno = parola[:int(lunghezzaParteUno)].upper()
parteDue = parola[int(lunghezzaParteUno):].upper()

composta = parteDue[::-1] + parteUno

print(f"La parola {parola} è lunga, {len(parola)}")
print(f"La prima parte è {parteUno} ed è lunga, {len(parteUno)}")
print(f"La seconda parte è {parteDue} ed è lunga, {len(parteDue)}")
print(f"La parola composta è, {composta.lower()}")
