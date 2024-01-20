# Leandro Gridelli

file = open("mtb.txt","w")

while True:
    giorno = input("Inserisci il giorno dell'anno: ")
    km = input("Inserisci i kilometri: ")
    dislivello = input("Inserisci il dislivello: ")
    tempo = input("Inserisci il tempo impiegato: ")

    file.write(giorno + "," + km + "," + dislivello + "," + tempo + "\n")

    continua = input("Continuare? (si/no): ")
    if continua == "no":
        break

file.close()
