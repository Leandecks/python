# Leandro Gridelli

def ultime_lettere(parola, lista):
    for p in lista:
        if p[-3:] == parola[-3:]:
            print(p)

# main

lista = ["Naso","Caso","Casa"]
parola = input("Inserisci una parola: ")

ultime_lettere(parola, lista)