# Leandro Gridelli

leggo_file = open("test01.txt","r")
testo = leggo_file.read()
leggo_file.close()
print(testo,"\n")
print(len(testo))

print()

telefono = open("telefono.txt")
riga1 = telefono.readline()
riga2 = telefono.readline()
telefono.close()
print(f"Riga 1: {riga1[:-1]}") # oppure ,end=""
print(f"Riga 2: {riga2[:-1]}")

print()

telefono = open("telefono.txt")
for riga in telefono:
   print(riga, end="")
telefono.close()

print()

telefono = open("telefono.txt")
lista = telefono.readlines()
telefono.close()
print(lista)
