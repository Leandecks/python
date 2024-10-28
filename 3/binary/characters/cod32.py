# Leandro Gridelli

ins = int(input("Inserisci un code point: "))

for k in range(ins, ins + 25):
    print(f"Decimale: {k}\tCode point: {hex(k)}\tCarattere: {chr(k)}")
    