# Gridelli Leandro 1E N16 03 - giorni

giorno = int(input("Immetti giorno: "))
mese = int(input("Immetti mese: "))

print(f"oggi è il {giorno}/{mese}/2021")

if (mese == 4 or mese == 6 or mese == 9 or mese == 11) and giorno == 30:
    print(f"DOMANI sarà il 1/{mese+1}/2021")
elif mese == 2 and giorno == 28:
    print(f"DOMANI sarà il 1/{mese+1}/2021")
elif mese == 12 and giorno == 31:
    print(f"anno concluso, DOMANI sarà il 99/99/2021")
elif (mese == 1 or mese == 3 or mese == 5 or mese == 7 or mese == 8 or mese == 10) and giorno == 31:
    print(f"DOMANI sarà il 1/{mese+1}/2021")
else:
    print(f"DOMANI sarà il {giorno+1}/{mese}/2021")
