# Leandro Gridelli

'''
Media, moda, mediana

Crea un programma che fa inserire una lista di numeri.
Viene calcolata la media.
Viene trovata la moda.
Nella posizione della mediana della lista viene inserita una barra |.
'''

# Inserimento

lista = []

while True:
  inserimento = input("Inserisci un numero: ")
  if str(inserimento) == "q":
    break
  lista.append(int(inserimento))

print()

# Media

media = 0

for k in lista:
  media += k

media = media / len(lista)

print(f"La media è {media}")

# Moda

quantita = 0
moda = 0

for k in lista:
  if quantita < lista.count(k):
    quantita = lista.count(k)
    moda = k

print(f"La moda è {moda}")

# Mediana

listaOrdinata = sorted(lista)
lenLista = len(listaOrdinata)

if len(listaOrdinata) % 2 == 0:
  lista.insert(lenLista // 2, "|")
else:
  lista[(lenLista-1)//2] = "|"

print(f"La mediana è lì: {lista}")