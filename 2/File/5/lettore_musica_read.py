# Leandro Gridelli

file = open("brani.txt")

print("tempo\tartista\t\tbrani")

massimo = 0

for riga in file:
   riga = riga.strip("\n").split(":")
   print(f"{riga[0]}:{riga[1]}\t{riga[2]}\t{riga[3]}")
   tempo = (int(riga[0]) * 60) + int(riga[1])

   if tempo > massimo:
      massimo = tempo
      brano_piu_lungo = riga[3].strip("\n")

print(f"\nIl brano più lungo è {brano_piu_lungo} di {massimo // 60}min {massimo % 60}sec")

file.close()
