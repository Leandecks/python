# Leandro Gridelli

frase = input("Inserisci una frase: ")

risultato = ''

for lettera in frase:
    if lettera in "ae":
        risultato = risultato + "X"
    else:
        risultato = risultato + lettera

print(risultato)
