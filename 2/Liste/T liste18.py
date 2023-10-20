# Leandro Gridelli

a = [1,3,5,2,3]
a.append(5)

print(a)
# a.append(4,7) # errore
a.append([4,7,5]) #aggiunge un elemento
print(a)

a = [3,1,3]
a.extend([4,5,7]) # aggiunge tanti elementi
print(a)

print()

s = ["Ferrari","Lotus","Mercedes","McLaren"]
s.append("Red Bull") # sempre in fondo
print(s)

s.insert(2, "Honda") # scelta della posizione
print(s)

s.extend(["Toyota","Alpine"])
print(s)

s.sort() # pesante
print(s)

print()

a = [3,1,5,2]
a.sort() # sovrascrizione di una stessa lista
print(a)

b = [3,1,5,2]
# c = b.sort() # non va
c = sorted(b) # nessuna modifica di b
print(c)

print()

a = [4,3,'a']
# a.sort() # impossibile
a = ['4','3','a']
a.sort() # ordine ascii
print(a)

a = ['13','2','21']
a.sort() # ordine ascii come per stringhe
print(a)

print()

frase = "Respiri piano per non far rumore"
a = list(frase)
print(a)

a = frase.split()
print(a)
a.sort()
print(a)

b = frase.split("i") # rimuove le i e taglia in quei punti
print(b)
b = frase.split("e")
print(b)

print()

f = "31;42;33;29;32;38"
temperature = f.split(";")
print(temperature)

print()

a = [1,2,3,4]
a.remove(3)
print(a)

##del a # tutto a
del a[1]
print(a)

print()

frase = "Respiri piano per non far rumore"
a = frase.split(" ")
print(a)
d = "-".join(a)
print(d)

print()

s = ["Ferrari","Lotus","Mercedes","McLaren"]
elemento = s.pop()
print(elemento)
print(s)
