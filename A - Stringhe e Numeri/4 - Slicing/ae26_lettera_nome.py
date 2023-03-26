# Leandro Gridelli

n=input("Inserisci il tuo nome: ")
c=input("Inserisci il tuo cognome: ")

parola=c[-2:]+n[::2]
par=parola[2].upper()
p=parola[0:2].lower()+par+parola[3:].lower()

print(p)
