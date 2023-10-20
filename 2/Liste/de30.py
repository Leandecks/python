# Leandro Gridelli

n=[1,2,3,4,5,6,7,6,5,4,3,3,1,3,4,5]
nuova = []

for k in range(len(n)):
  if k%2==0:
    nuova.append(n[k])
  else:
    nuova.append("X")

print(nuova)