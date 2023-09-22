# Leandro Gridelli

'''
Data una parola, il programma sostituisce le vocali con dei +
e le consonanti con dei -
'''

parola = input("Inserisci parola: ")

vocali = "aeiou"

risultato = ''

for lettera in parola:
    if lettera in vocali:
        risultato += "+"
    else:
        risultato += "-"

print(risultato)
