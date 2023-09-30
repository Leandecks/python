# Leandro Gridelli

a = [100,4,1,10,1,9,6,6]

M = a[0]
m = a[0]

# modo 1

print("Massimo:", max(a))
print("Minimo:", min(a))

# modo 2

for k in a:
   if k > M:
      M = k
   elif k < m:
      m = k

print("Il massimo è",M)
print("Il minimo è",m)
