# Leandro Gridelli

file = open("punti.txt")

rapporto_max = 0

for riga in file:
   riga = riga.strip("\n").split(",")
   rapporto = int(riga[1]) / int(riga[2])
   if rapporto > rapporto_max:
      rapporto_max = rapporto
      nome_vincitore = riga[0]
      punti_vincitore = riga[1]
      tempo_vincitore = int(riga[2])
      ore_vincitore = tempo_vincitore // 60
      minuti_vincitore = tempo_vincitore % 60

file.close()
print("THE WINNER IS...")
print(f"*** {nome_vincitore.upper()} ***")
print(f"Punti: {punti_vincitore}")
print(f"Tempo: {ore_vincitore}h{minuti_vincitore}min")
print(f"Rapporto: {round(float(rapporto_max), 4)}")
