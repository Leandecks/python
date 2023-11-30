# Leandro Gridelli

passi = open("passi.txt")
totale_passi = 0 
nr_righe = 0

print("giorno\tmese\tanno\tpassi")

for riga in passi:
  riga = riga.strip("\n")
  riga = riga.split(":")
  riga[0] = riga[0].split("-")

  totale_passi += int(riga[1])
  nr_righe += 1
  
  print(riga[0][0] + "\t" + riga[0][1] + "\t" + riga[0][2] + "\t" + riga[1])

media = round((totale_passi / nr_righe), 1)

print()
print(f"Totale passi: {totale_passi}")
print(f"Media giornaliera: {media} passi")