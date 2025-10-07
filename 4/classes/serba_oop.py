# Leandro Gridelli

class Serbatoio(object):
    def __init__(self, c, l):
        self.capienza = c
        self.livello = l
        
    def __str__(self):
        return f"La capienza è {self.capienza}\nIl livello è {self.livello}"
    
    def vuota(self):
        self.livello = 0
    
    def pieno(self):
        self.livello = self.capienza
        
    def stampa_livello(self):
        return self.livello
    
    def aggiungi(self, n):
        self.livello += n
        
    def togli(self, n):
        self.livello -= n
        
# main

serba = Serbatoio(100, 50)
        
while True:
    print(str(serba), "\n")
    azione = input("Scegli azione:\na - aggiungi\np - preleva\nv - vuota\nf - fai il pieno\nq - esci\n\n> ")

    if azione == "q":
        break
    elif azione == "a":
        inp = int(input("\nQuanto vuoi aggiungere: "))
        serba.aggiungi(inp)
    elif azione == "p":
        inp = int(input("\nQuanto vuoi aggiungere: "))
        serba.togli(inp)
    elif azione == "v":
        serba.vuota()
    elif azione == "f":
        serba.pieno()