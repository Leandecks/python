# Leandro Gridelli

passi = open("passi.txt","w")

while True:
  giorno = input("Inserisci il giorno: ")
  mese = input("Inserisci il mese: ")
  anno = input("Inserisci l'anno: ")
  passi_giornalieri = input("Inserisci i passi di oggi: ")
  avanti = input("Vuoi inserire un altro giorno? (si/no) ")

  passi.write(giorno + "-" + mese + "-" + anno + ":" + passi_giornalieri + "\n")

  if avanti == "no":
    break

passi.close()