# Leandro Gridelli

file = open("campionato.txt","w")

nome = input("Inserisci il nome: ")
cognome = input("Inserisci il cognome: ")
campionato = input("Inserisci il campionato: ")
goal = input("Inserisci i goal: ")
tiri_porta = input("Inserisci i tiri in porta: ")
passaggi = input("Inserisci i passaggi: ")
minuti = input("Inserisci i minuti giocati: ")
km = input("Inserisci i kilometri percorsi: ")

file.write(nome + "," + cognome + "," + campionato + "," + goal + "," + tiri_porta + "," + passaggi + "," + minuti + "," + km + "\n")

file.close()