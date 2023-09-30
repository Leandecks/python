# Leandro Gridelli

media = 0
massimo = []
minimo = []

x = int(input("Quanti numeri vuoi: "))

for k in range(x):
   n = input("Inserisci numero: ")
   if str(n) == "q":
      break
   n = int(n)
   media += n
   massimo.append(n)
   minimo.append(n)

media = media / x
massimo = max(massimo)
minimo = min(minimo)
 
print(f"La media è {round(media)}")
print(f"Il massimo è {massimo}")
print(f"Il range è {massimo-minimo}")
