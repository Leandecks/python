# Leandro Gridelli

import random

def crea_dizionario():
    diz = {}
    for k in range(4):
        data = input("Inserisci la data: ")
        max_tavoli = int(input("Inserisci massimo di tavoli: "))
        n_prenotazioni = int(input("Quante prenotazioni ci sono il " + data + " ? "))
        tavoli = set()
        
        for k in range(n_prenotazioni):
            tavolo = input("Inserisci il nome per la prenotazione del tavolo: ")
            n_tavolo = random.randint(1, max_tavoli)
            tavoli.add((n_tavolo, tavolo))
            
        diz[data] = (max_tavoli, tavoli)
    return diz

def prenota(diz):
    data = input("Inserisca la data per la prenotazione: ")
    nome = input("Inserisca il nome per la prenotazione: ")
    
    if data in diz:
        diz[data][1].add((random.randint(1, diz[data][0]), nome))
    else:
        diz[data] = (random.randint(1, diz[data][0]), nome)
        
# main

diz = {'2024-04-05': (10, {(2, 'Bartolini'), (9, 'Crinelli'), (7, 'Maioli'), (4, 'Sacchetti')}), '2024-07-16': (2, {(2, 'Lucchi')}), '2024-05-25': (8, {(7, 'Gridelli'), (6, 'Vignoli'), (1, 'Bonetti')}), '2024-12-01': (15, {(1, 'Gonzalez'), (13, 'Magnani')})}

# print(crea_dizionario())

prenota(diz)
print(diz)
