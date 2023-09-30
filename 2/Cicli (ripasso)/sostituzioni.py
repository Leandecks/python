# Leandro Gridelli

frase = input("Inserisci una frase: ")

frase = "X" + frase[1:-1] + "X"

risultato = ''

for k in range(len(frase)):
   if k%5==0 and k!=0:
      risultato += str(k)
   else:
      risultato += frase[k]

print(risultato)
