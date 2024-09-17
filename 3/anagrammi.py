# Leandro Gridelli

import random

def fattoriale(numero):
    fact = 1
    for k in range(1, numero + 1):
        fact *= k
    return fact

def doppie(stringa):
    diz_doppie = {}
    for lettera in stringa:
        if stringa.count(lettera) > 1:
            diz_doppie[lettera] = stringa.count(lettera)
    return diz_doppie

def combinazioni(stringa):
    """
    (str) -> int

    Calcola il numero di combinazioni possibili di lettere in una parola (formando anagrammi).
    Utilizzando la formula:
    L! / d1! * d2! * ... * dn!
    dove:
    L = lunghezza della parola
    d1, d2, ..., dn = ripetizione delle varie doppie
    ! = fattoriale
    """
    fattoriale_eccessivo = fattoriale(len(stringa))
    lista_quantita_lettera_doppie = list(doppie(stringa).values())
    prodotto_fattoriali_doppie = 1

    for quantita in lista_quantita_lettera_doppie:
        prodotto_fattoriali_doppie *= fattoriale(quantita)

    return round(fattoriale_eccessivo / prodotto_fattoriali_doppie)

def genera_permutazioni(parola_scelta, nr_fattoriale):
    lista_permutazioni = []

    while len(lista_permutazioni) < nr_fattoriale:
        stringa = ""
        while len(stringa) < len(parola_scelta):
            scelta = random.choice(parola_scelta)
            while stringa.count(scelta) + 1 > parola_scelta.count(scelta):
                scelta = random.choice(parola_scelta)

            stringa += scelta

        if stringa not in lista_permutazioni:
            lista_permutazioni.append(stringa)

    return lista_permutazioni

def trova_parole(nome_file, lista_permutazioni):
    parole_corrette = []

    for riga in open(nome_file, encoding = "utf-8"):
        parola_italiana = riga.strip("\n")
        for parola_eventuale in lista_permutazioni:
            if parola_eventuale == parola_italiana:
                parole_corrette.append(parola_eventuale)

    return parole_corrette

# main

parola = input("Inserisci la stringa di almeno 3 lettere: ")
nr_permutazioni = combinazioni(parola)

print(f"Le permutazioni sono {nr_permutazioni}")
permutazioni = genera_permutazioni(parola, nr_permutazioni)
print(f"Ecco le possibili permutazioni {permutazioni}")
        
corrette = trova_parole("parole.txt", permutazioni)
print(f"Le parole valide rimaste sono: {corrette}")
