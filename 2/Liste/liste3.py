# Leandro Gridelli

a = [0,4,1,0,1,9,6,6]

# modo 1

for k,i in enumerate(a):
   if k%2==0:
      print(i)

# modo 2

print()
print()

for k in range(len(a)):
   if k%2==0:
      print(a[k])
