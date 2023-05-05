# Leandro Gridelli

'''
Data una parola immessa da tastiera scrivi un programma che indica se la parola contiene la lettera h

Data una parola immessa da tastiera scrivi un programma che indica quante lettere e sono presenti nella parole
'''

p = input("Imetti una parola: ")

for k in p:
    if k == "h":
        print("La parola contiene una h")
    else:
        print("La parola non contiene h")
