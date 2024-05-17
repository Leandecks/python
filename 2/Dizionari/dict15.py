# Leandro Gridelli

def aggiungi():
    volte = int(input("Quanti dati vuoi inserire: "))

    for k in range(volte):
        data = input("Inserisci la data: ")
        nr_clienti = int(input("Quanti clienti vuoi inserire: "))
        clienti = []

        for i in range(nr_clienti):
            cliente = input("Inserisci il nome del cliente: ")
            clienti.append(cliente)

        prenotazioni[data] = clienti


def rimuovi():
    data = input("Inserisci la data: ")
    cliente = input("Inserisci il cliente: ")
    prenotazioni[data].remove(cliente)


def visualizza():
    data = input("Inserisci la data: ")
    print(prenotazioni[data])


# Main

# prenotazioni = {
#     "15/09/2024": ["Marco", "Matteo","Luca"]    
# }

prenotazioni = {
    '15/09/2024': ['Marco', 'Matteo', 'Luca'],
    '01/01/2025': ['Righetti', 'Ghisolfi', 'Rossi', 'Bianchi'],
    '07/12/2024': ['Verdi', 'Vignoli'],
    '02/02/2026': ['Leo', 'Giova', 'Michi', 'Thomas', 'Clara', 'Michael'],
    '17/07/2024': ['Lucchi']
}

aggiungi()
rimuovi()
visualizza()

print(prenotazioni)
