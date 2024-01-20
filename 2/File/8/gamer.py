# Leandro Gridelli

file = open("punti.txt","w")

for k in range(4):
   nickname = input("Inserisci il nickname: ")
   punteggio = input("Inserisci il punteggio: ")
   tempo = input("Inserisci il tempo: ")

   file.write(nickname + "," + punteggio + "," + tempo + "\n")

file.close()
