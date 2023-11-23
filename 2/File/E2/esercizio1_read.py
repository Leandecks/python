# Leandro Gridelli

'''
Lo script legge il file generato con i numeri primi e li stampa all'utente sotto forma di lista
'''

file = open("primi.txt")
primi = file.readlines()
lista = []
for primo in primi:
  primo = primo[:-1]
  lista.append(primo)

print(lista)
file.close()