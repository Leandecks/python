# Leandro Gridelli

frase = input("Inserisci una frase: ")

risultato = ''

for k in range(len(frase)):
    if k==0 or k==len(frase)-1:
        risultato+="5"
    elif k%2==0:
        risultato+=frase[k].upper()
    else:
        risultato+=frase[k].lower()

print(risultato)
