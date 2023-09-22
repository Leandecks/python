# Leandro Gridelli

print("Inserisci i dati della prima puntata:")
p1_ore = int(input("Ore: "))
p1_min = int(input("Minuti: "))

print("Inserisci i dati della seconda puntata:")
p2_ore = int(input("Ore: "))
p2_min = int(input("Minuti: "))

print("Inserisci i dati della terza puntata:")
p3_ore = int(input("Ore: "))
p3_min = int(input("Minuti: "))

tempo_totale = (p1_ore+p2_ore+p3_ore)*60 + (p1_min+p2_min+p3_min)
ore = tempo_totale // 60
minuti = tempo_totale % 60

print(f"Per vedere tutte e 3 le puntate impiegherai {tempo_totale} minuti cioé {ore}:{minuti} ore")
