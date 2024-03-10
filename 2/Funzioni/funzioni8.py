# Leandro Gridelli

'''
Scrivi un programma che acquisisce in input una lista di parola, controllando che siano composte da soli caratteri alfabetici,
poi implementa una procedura che legge la lista, scrive sul monitor una parola per riga ed accanto in numero di vocali e di consonanti che la compongono.
Se la parola contiene la lettera H deve essere scritta in maiuscolo, mentre se non la contiene, in minuscolo.
'''

vocali = "aeiou"

def vocalizza(lista):
    for parola in lista:
        voc = 0
        cons = 0
        
        for lettera in parola:
            if lettera in vocali:
                voc += 1
            else:
                cons += 1
                
        if "h" in parola.lower():
            parola = parola.upper()
        else:
            parola = parola.lower()
        
        print(f"{parola}: {voc} vocali, {cons} consonanti")

# main

list = []

while True:
    inserimento = input("Inserisci una parola: ")
    if not inserimento.isalpha():
        continue
    elif inserimento == "q":
        break
    list.append(inserimento)
    
vocalizza(list)