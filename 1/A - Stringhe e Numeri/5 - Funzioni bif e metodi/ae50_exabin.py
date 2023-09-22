# Leandro Gridelli

dec = int(input("Inserisci un numero decimale: "))
bin = bin(dec).strip("0b")
hex = hex(dec).strip("0x")

print("Il numero in binario è:",bin)
print("Il numero in esadecimale è:",hex)