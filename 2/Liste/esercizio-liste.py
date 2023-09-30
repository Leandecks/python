# Leandro Gridelli

'''
Crea uno script che acquisisce tanti numeri quanti scelti dall'utente e poi li aggiunge a una lista e determina la media, il massimo, il minimo, il range ed esegue con una
funzione la moltiplicazione fra il primo e l'ultimo numero della lista
'''

volte = int(input("Quanti numeri vuoi inserire? "))

numeri = []
media = 0

for k in range(volte):
   x = int(input("Inserisci un numero: "))
   numeri.append(x)

for i in numeri:
   media += i

media = round(media / i)
massimo = max(numeri)
minimo = min(numeri)
range = massimo - minimo

primo = numeri[0]
ultimo = numeri[-1]


def moltiplica(a,b):
   return a*b


risultato = moltiplica(primo,ultimo)

print("Media:",media)
print("Massimo:",massimo)
print("Minimo:",minimo)
print("Range:",range)
print("Risultato moltiplicazione:",risultato)
