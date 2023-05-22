# Leandro Gridelli

frase = input("Inserisci una frase: ")

risultato = ''

for k in range(len(frase)):
    if k%5 == 0 and k!=0:
        risultato += "X"
    else:
        risultato += frase[k]

print(risultato)
