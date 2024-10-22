# Leandro Gridelli

with open("cod21.txt", "w", encoding = "iso-8859-1") as file:
    for k in range(160, 250):
        file.write(chr(k))

ins = "ISO-8859-" + input("Inserisci numero da 1 a 16: ")

with open("cod21.txt", "r", encoding = ins, errors = "ignore") as file2:
    for k in range((250 - 160) // 30):
        print(file2.read(30))
