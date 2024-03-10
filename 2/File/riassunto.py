'''
E012 metodi

questo non è un programma, ma riassume i metodi visti di scrittura e lettura su file

RICAPITOLANDO:
.readline()  	legge una riga alla volta (ricorda dove è arrivato)
.readlines() 	legge il file e costruisce una lista con un elemento per riga
.read()		legge l'intero file e lo mette in una stringa
.read(N)		leggi i primi N bytes (e sposta il cursore avanti di N posti)
.write(testo)	scrive il testo sul file, deve essere sempre di tipo string
.writelines(testo)	scrive il testo sul file, ha come argomento un iterabile
                                         (esempio tupla, lista, stringa o altro)
.seek(n): set streamer position n
.tell(): return streamer position
'''
