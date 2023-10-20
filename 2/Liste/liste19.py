# Leandro Gridelli

stringa = input("Inserisci una stringa: ")

consonanti = "bcdfghjklmnpqrstvwxyz"
vocali = "aeiou"

c = []
v = []

for k in stringa:
   if k in consonanti:
      if k.upper() not in c:
         c.append(k.upper())
   elif k in vocali:
      if k.upper() not in v:
         v.append(k.upper())

c = sorted(c)
v = sorted(v)

print(f"Le consonanti sono: {c}")
print(f"Le vocali sono: {v}")
