# Leandro Gridelli

def stampa_diz(dizionario):
    for chiave in dizionario:
        print(chiave, "    ", dizionario[chiave])

# main

cantina = {
    "Albana": 100,
    "Barbera": 35,
    "Chianti": 57,
    "Amarone": 15
}

# delete

del cantina["Amarone"]
stampa_diz(cantina)
print()

# add

cantina["Barolo"] = 13
stampa_diz(cantina)
print()

# change

cantina["Albana"] -= 4
stampa_diz(cantina)
print()

# amount of keys

print(len(cantina))

# total amount of values

# print(sum(cantina.values()))

bottiglie = 0
for k in cantina:
    bottiglie += cantina[k]
    
print(bottiglie)

chiavi = []
for k in cantina:
    chiavi.append(k)
print(chiavi == list(cantina.keys()))

print()

items = list(cantina.items())
print(items)

print()

lista = ["a", "b", "c"]
for i, j in enumerate(lista):
    print(i, j)
    
print()
    
for k, v in cantina.items():
    print(k, v)
