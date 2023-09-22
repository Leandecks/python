# Leandro Gridelli

f = input("Inserisci frase: ")

c = ''
d = ''

voc = "aeiou"
con = "bcdfghjklmnpqrstvwxyz"

''' ALTERNATIVA
for pos,lettera in enumerate(s):
   if pos%2==0 and lettera in con...
'''

for k in range(len(f)):
   if k%2==0 and f[k] in con:
      c += f[k]
   elif k%2!=0 and f[k] in voc:
      d += f[k]

print("Consonanti:",c)
print("Vocali:",d)

last_c = c[:3]
last_c += "   "
last_c = last_c[:3]

if last_c[0] == last_c[1] ==  last_c[2]:
   last_c = last_c[0]
elif last_c[0] == last_c[1]:
   last_c = last_c[0] + last_c[2]
elif last_c[1] == last_c[2]:
   last_c = last_c[0] + last_c[1]
elif last_c[0] == last_c[2]:
   last_c = last_c[0] + last_c[1]
   
last_d = d[-3:]

risultato = ''

for k in range(3):
   if len(last_c) < 3:
      last_c += "XXX"
   if len(last_d) < 3:
      last_d += "XXX"
   risultato += last_c[k]
   risultato += last_d[k]

print("Risultato:",risultato)
