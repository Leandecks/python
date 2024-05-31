# Leandro Gridelli

'''
Elementi non ripetuti, ordine casuale, mutabile (=> non chiave per dizionario). Parentesi graffe
'''

s = set("casa")
a = {1, 2, 3}

print(s)
print(type(a))

a.add("z") # come append
print(a)

a.update(s) # unire set
print(a)

a.discard(3) # togliere elemento, se non c'è non da errore
print(a)

a.remove("a") # togliere elemento, se non c'è da errore
print(a)

x = {1, 2, 3}
y = {1, 2, 5, 6}
i = x.intersection(y)
u = x.union(y)
d = x.difference(y) # X - Y

print(i, u, d)
