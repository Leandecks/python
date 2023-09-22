# Leandro Gridelli

c=input("Immetti il tuo cognome: ")
v=input("Immetti la tua via: ")
n=int(input("Immetti il tuo numero di casa: "))

codice=c[0]+c[-1]+str(n**2)+v[::2]
print(codice)
