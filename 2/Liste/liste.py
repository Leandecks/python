# Leandro Gridelli

lista = [2]
ln = [3,4,5,6,7]
ls = ["Mario","Luigi","Boo"]

print(lista,ln,ls)

lm = [3,5,6,3.14,8,[],"teorema di Euclide",[1,2,3]]

print()

print(lm)
print()
print(ls[1])
print()
print(ln[4], ln[-1])
print()

##print(ln[8]) Index out of range
##print(ln[2.3]) Float non accettati

print(ln[2:4])
print()
print(ln[2-4])
print()

for k in ls:
   print(k)

print()

for k in range(len(ls)): # range(3) = 0-2
   print(k)

print()

for k in range(len(ls)): # range(3) = 0-2
   print(k, ls[k]) # come enumerate

print()

for p,e in enumerate(ls):
   print(p, e)

print()

s = "arcobaleno"
print(s[4])
##s[4] = "m" La stringa è immutabile

print()

print(ls)
ls[1] = "Bowser" # La lista è mutabile
print(ls)

