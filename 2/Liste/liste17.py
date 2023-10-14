# Leandro Gridelli

stringa = input("Inserisci una stringa: ")
list(stringa)

consonanti = "BCDFGHJKLMNPQRSTVWXYZ"
vocali = "AEIOU"
v = []
c = []

for k in stringa:
   k = k.upper()
   if k in vocali and k not in v:
      v.append(k)
   elif k in consonanti and k not in c:
      c.append(k)

c = sorted(c)
v = sorted(v)

print(list(c))
print(list(v))
