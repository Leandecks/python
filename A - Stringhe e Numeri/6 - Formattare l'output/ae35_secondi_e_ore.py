# Leandro Gridelli

secondi = int(input("Inserisci il nr di secondi: "))

ore = secondi // 3600
minuti = secondi % 3600 // 60
sec = secondi - (ore*3600) - (minuti*60)

print(f"Ore: {ore}\nMinuti: {minuti}\nSecondi: {sec}")