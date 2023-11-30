# Leandro Gridelli

file = open("nuoto.txt","w")


volte = int(input("Quanti atleti vuoi inserire? "))

for k in range(volte):
   print("Prossimo atleta")
   nome = input("Inserisci il nome: ")
   cognome = input("Inserisci il cognome: ")
   eta = input("Inserisci l'età: ")
   vasche = input("Inserisci le vasche: ")
   stile = input("Inserisci lo stile: ")
   minuti = input("Inserisci i minuti: ")

   file.write(nome + ",")
   file.write(cognome + ",")
   file.write(eta + ",")
   file.write(vasche + ",")
   file.write(stile + ",")
   file.write(minuti + "\n")

file.close()
