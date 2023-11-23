# Leandro Gridelli

file = open("test01.txt","w")
file.write("Il mio primo file\n")
file.write("Scritto in python\nda Leandro")
file.close()
print("Ho appena scritto un file")

telefono = open("telefono.txt","w")
for k in range(3):
   nome = input("Immetti nome: ")
   tel = input("Immetti telefono: ")
   telefono.write(nome + ";" + tel + "\n")
telefono.close()
