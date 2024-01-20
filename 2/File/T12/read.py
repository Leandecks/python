# Leandro Gridelli

file = open("Prova.txt")

stringa1 = file.read(8) # read chars

file.seek(4) # pointer to selected char

stringa2 = file.read(10)
stringa3 = file.read(1000) # no out of bounds; prints the rest

print(stringa1)
print(stringa2)
print(stringa3)

print(file.tell()) # returns pointer position

file.close()