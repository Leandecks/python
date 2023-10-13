# Leandro Gridelli

a = input("Inserisci una serie di numeri: ")
a = list(a)

pari = []
dispari = []

for k in a:
   if int(k)%2==0:
      pari.append(k)
   else:
      dispari.append(k)

print(f"Numeri: {a}")
print(f"Pari: {pari}")
print(f"Dispari: {dispari}")

if len(pari) == len(dispari):
   print("Ci sono tanti pari quanti dispari") 
elif len(pari) > len(dispari):
   print("Ci sono piu numeri pari")
else:
   print("Ci sono piu numeri dispari")
