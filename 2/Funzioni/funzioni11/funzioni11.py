# Leandro Gridelli

'''
Implementa una funzione che, ricevuto in input una lista di parole e una parola singola,
cerca tutte le parole dell'elenco che hanno le ultime 3 lettere uguali alla parola inserita.

Utilizza poi la funzione per cercare la rima di una parola inserita utilizzando come elenco parole il file parole.txt,
riportato sotto, che contiene tutte le parole della lingua italiana.
'''


def rima(parole_da_cercare, parola_da_rimare):
    return [p for p in parole_da_cercare if p[-3:] == parola_da_rimare[-3:]]
    # rime = []
    # for p in lista:
    #     if p[-3:] == parola[-3:]:
    #         rime.append(p)
    #
    # return rime


# main

# lista = []

# while True:
#     inserimento = input("Inserisci una parola per la lista / q per terminare: ")
#     if inserimento == "q":
#         break
#     else:
#         lista.append(inserimento)

parola = input("Inserisci una parola per cercare la rima: ")

# print(rima(lista, parola))

# file

dizionario = [riga.strip("\n") for riga in open("parole.txt")]
# dizionario = []
# for riga in open("parole.txt"):
#     dizionario.append(riga.strip("\n"))

print(rima(dizionario, parola))
