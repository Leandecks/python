# Leandro Gridelli

print("Immetti i tuoi dati")
n=input("Nome: ")
c=input("Cognome: ")

codice=n[1::2]+c[::-2]+str(len(n)**len(c))
print(codice.upper())
    
