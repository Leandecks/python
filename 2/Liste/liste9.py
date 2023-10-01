# Leandro Gridelli

a =  [1,2,4,6,7]
b = [3,2,1,6,3]
risultato = 0

for i,k in enumerate(a):
   if k == b[i]:
      print(f"Elemento corrispondente {k} in posizione {i}")
      risultato += 1

print(f"Risposta: {risultato}")