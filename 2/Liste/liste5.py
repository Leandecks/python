# Leandro Gridelli

a = [0,4,1,0,1,9,6,6]

d = 0
p = 0

for k in a:
   if k%2==0:
      p += k
   else:
      d += k

print(f"Somma numeri pari: {p}")
print(f"Somma numeri dispari: {d}")
