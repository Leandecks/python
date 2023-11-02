# Leandro Gridelli

'''
Il seguente programma prende 2 liste inserite da tastiera e crea una terza lista formata dagli elementi in comune.
Tutti i numeri di questa lista vengono trasformati in esadecimali e riscritti al contrario.
Viene scritta a video questa lista elaborata tranne il primo e l'ultimo elemento.
'''

a = []
b = []
c = []

while True:
  inserimento = input("Inserisci un numero per la lista a: ")
  if inserimento == "q":
    break
  a.append(int(inserimento))

while True:
  inserimento = input("Inserisci un numero per la lista b: ")
  if inserimento == "q":
    break
  b.append(int(inserimento))

for k in a:
  if k in b:
    k = ''.join(reversed(hex(k)))
    c.append(k)

del c[-1]
del c[0]

print(f"Lista A: {a}")
print(f"Lista B: {b}")
print(f"Lista Risultato: {c}")