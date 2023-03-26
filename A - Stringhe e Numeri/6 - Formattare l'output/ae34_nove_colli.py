# Leandro Gridelli

ore = int(input("Inserisci il nr di ore: "))
minuti = int(input("Inserisci il nr di minuti: "))
sec = int(input("Inserisci il nr di secondi: "))

totaleSecondi = sec + minuti*60 + ore*3600

print(f"Il totale in ore è {totaleSecondi}")