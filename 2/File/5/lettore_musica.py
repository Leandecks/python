# Leandro Gridelli

file = open("brani.txt","w")

tempo = 0

print("Inserimento brani:")

while True:
   minuti = input("Inserisci i minuti: ")
   secondi = input("Inserisci i secondi: ")
   artista = input("Inserisci l'artista: ")
   brano = input("Inserisci il brano: ")

   tempo += int(secondi) + (int(minuti) * 60)
   tempo_rimanente = 3600 - tempo

   if tempo > 3600:
      print(f"Hai superato il limite (sei a {tempo // 60}min, {tempo % 60}sec)")
      print("Il brano non sarà inserito")
      break
   else:
      print(f"Ti mancano: {tempo_rimanente // 60}min, {tempo_rimanente % 60}sec")
      file.write(minuti + ":" + secondi + ":" + artista + ":" + brano + "\n")

   proseguire = input("Vuoi inserire un altro brano? (si/no) ")

   if proseguire == "no":
      break

file.close()
