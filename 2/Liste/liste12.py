# Leandro Gridelli

a = [1,2,5,6,0]
b = [3,5,6,6,7]

corrispondenti = False

for k in range(len(a)):
   if a[k] == b[k]:
      corrispondenti = True
      break # più veloce

if corrispondenti:
   print("Ci sono elementi corrispondenti")
else:
   print("Gli elementi sono diversi")
