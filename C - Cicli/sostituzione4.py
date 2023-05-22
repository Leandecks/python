# Leandro Gridelli

'''
Programma sostituisce gli elementi in posizione pari con +
e i multipli di 5 con dei -
se una lettera è multipla sia di 5 che di 2 non viene sostituita
'''

frase = input("Inserisci una frase: ")

risultato = ''

for k in range(len(frase)):
    if k%2==0 and k%5==0 and k!=0:
        risultato += frase[k]
    elif k%2==0:
        risultato += "+"
    elif k%5==0:
        risultato += "-"
    else:
        risultato += frase[k]

print(risultato)
