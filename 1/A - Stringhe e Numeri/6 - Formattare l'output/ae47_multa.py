# Leandro Gridelli

""" ingresso = float(input("Ore di ingresso a scuola: "))

minutiIngresso = (ingresso - 8) * (5/3)

multaCent = minutiIngresso * 3

multaEuro = multaCent // 100

multaCentesimi = multaEuro % 100

print("MULTA: Euro={multaEuro}, Centesimi={multaCentesimi}")

print(minutiIngresso) """


ingresso=float(input("ora di ingresso -> ")) # float perchè inserito con la virgola

ritardo= ingresso -8                #calcolo il ritardo ripetto all'ora di ingresso a scuola
 
ore  = ritardo // 1                     # prendo solo la parte intera dell'orario inserito
minuti=(ritardo-ore)*100        #calcolo i minuti 

multa=ore*60*3+minuti*3    # calcolo l'importo della multa in centesimi

euro=multa//100                         # trasformo in euro 
centesimi=multa-euro*100        # calcolo il resto incentesimi

print(f"multa {euro:2.0f} euro e {centesimi:2.0f} centesimi ")