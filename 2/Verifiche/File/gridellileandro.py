# Gridelli Leandro

# main

# scrittura file byte.txt

file_byte_write = open("byte.txt","w")

bytes_inseriti = []

for k in range(1,9):
    while True:
        inserimento = input(f"immetti byte riga n.{k}->>")
        
        corretto = True
        
        if not inserimento.isnumeric() or len(inserimento) != 8 or inserimento in bytes_inseriti:
            corretto = False
            
        for bit in inserimento:
            if int(bit) not in [0,1]:
                corretto = False
        
        if corretto:
            bytes_inseriti.append(inserimento)
            break
        else:
            print("Dato immesso non corretto - INSERIRE NUOVAMENTE")
        
            
for byte in bytes_inseriti:
    file_byte_write.write(byte + "\n")

file_byte_write.close()

# lettura file byte.txt

file_byte_read = open("byte.txt")

bytes_elaborati = []

for riga in file_byte_read:
    riga = riga.strip("\n")
    
    if riga.count("1") % 2 != 0:
        byte_elaborato = "X" + riga[1::]
        bytes_elaborati.append(byte_elaborato)
    else:
        bytes_elaborati.append(riga)

file_byte_read.close()

# scrittura file controllo pari.txt

file_controllo_pari = open("controllo pari.txt","w")

for byte in bytes_elaborati:
    if byte[0] == "X":
        file_controllo_pari.write(byte + "  : rilevato errore, numero di 1 dispari\n")
    else:
        file_controllo_pari.write(byte + "\n")       

file_controllo_pari.close()