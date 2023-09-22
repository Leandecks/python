# Leandro Gridelli

ore = int(input("Inserisci il nr di ore: "))
minuti = int(input("Inserisci il nr di minuti: "))
secondi = int(input("Inserisci il nr di secondi: "))

tot_sec = secondi+minuti*60+ore*3600

print("Il totale in secondi è:",tot_sec)

distanza = int(input("Inserisci la distanza totale: "))

tot_ore = tot_sec   / 3600
vMedia = distanza / tot_ore

print("La velocità media è",round(vMedia,2),"km/h")
