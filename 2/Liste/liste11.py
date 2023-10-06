# Leandro Gridelli

a = []
b = []
c = []

# modo con while

inserta = 0
inserta2 = 0

print("Inserisci i numeri per la lista a:")

while inserta != "q":
   inserta = input("Inserisci un numero: ")
   if inserta == "q":
      break
   else:
      a.append(int(inserta))
      
print("Inserisci i numeri per la lista b:")

while inserta2 != "q":
   inserta2 = input("Inserisci un numero: ")
   if inserta2 == "q":
      break
   else:
      b.append(int(inserta2))

##volte = int(input("Quanti numeri vuoi inserire? "))
##
##for k in range(volte):
##   inserta = int(input("Inserisci un numero: "))
##   a.append(inserta)
##
##volte = int(input("Quanti numeri vuoi inserire? "))
##
##for k in range(volte):
##   inserta = int(input("Inserisci un numero: "))
##   b.append(inserta)

c += a[:-1]
c += b[1:]

print(a)
print(b)
print(c)
