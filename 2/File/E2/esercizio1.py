# Leandro Gridelli

'''29
Scrivi un programma che crea un nuovo file che contiene tutti i numeri primi minori del numero inserito in input.
I primi sono separati da una virgola
es.

input = 10
output:
2
3
5
7
'''

volte = int(input("Inserisci un numero: "))
file = open("primi.txt","w")

non_primo = False

for n in range(2, volte):
  non_primo = False
  for k in range(2, n):
    if (n % k) == 0:
      non_primo = True
      break

  if not non_primo:
    file.write(str(n) + "\n")

file.close()