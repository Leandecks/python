# Leandro Gridelli

file = open("nuoto.txt")

somma = 0
minimo = 9999999999
massimo = 0
tempo = 0
tempo_massimo = 0

for riga in file:
   riga = riga.split(",")
   somma += int(riga[3])
   tempo += int(riga[-1])
   
   if int(riga[-1]) < minimo:
      minimo = int(riga[-1])
      veloce = riga[0]

   if int(riga[2]) > massimo:
      massimo = int(riga[2])
      anziano = riga[0]

   if int(riga[-1]) > tempo_massimo:
      tempo_massimo = int(riga[-1])
      nuotatore_dedicato = riga[0]
      nuotatore_dedicato_cognome = riga[1]

file.close()

minuti = tempo % 60
ore = tempo // 60
   
print(f"* Somma vasche: {somma}")
print(f"Tempo minimo di {minimo} minuti dell'atleta {veloce}")
print(f"Atleta più anziano: {anziano} di {massimo} anni")
print(f"* Tempo totale di allenamento: {ore}h {minuti}min")
print(f"* {nuotatore_dedicato} {nuotatore_dedicato_cognome} si è allenato per più tempo di tutti ({tempo_massimo} minuti)")
