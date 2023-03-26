# Leandro Gridelli

frase = input("Immetti una stringa a piacere: ")

print("Il carattere con valore ASCII massimo è", max(frase))
print("Il carattare con valore ASCII minimo è", min(frase))

print("Il codice ASCII di", max(frase),"è", ord(max(frase)))
print("Il codice ASCII di", min(frase),"è", ord(min(frase)))

range = ord(max(frase)) - ord(min(frase))
print("Il range è", range)