# Leandro Gridelli

file = open("campionato.txt")

km_max = 0

for riga in file:
    riga = riga.strip("\n").split(",")
    
    goal = int(riga[3])
    minuti = int(riga[-2])
    tiri = int(riga[4])
    km = int(riga[-1])
    
    if km > km_max:
        km_max = km
        giocatore_km_max = riga[0] + " " + riga[1]
    
    coefficiente_tempo = goal / minuti
    coefficiente_tiri = goal / tiri
    
    print(f"Coefficiente di realizzazione in base al tempo: {coefficiente_tempo}")
    print(f"Coefficiente di realizzazione in base ai tiri: {coefficiente_tiri}\n")

print(f"Giocatore che ha percorso più km: {giocatore_km_max} con {km_max}")

file.close()