# Leandro Gridelli

class Lavoratore(object):
    def __init__(self, codice, nominativo, livello):
        self.codice = codice
        self.nominativo = nominativo
        self.livello = livello
        
    def __str__(self):
        a = "\nCodice: " + str(self.codice)
        b = "\nNominativo: " + str(self.nominativo)
        c = "\nLivello: " + str(self.livello)
        
        return a + b + c
    
class Operaio(Lavoratore):
    def __init__(self, codice, nominativo, livello, reparto, capoReparto):
        Lavoratore.__init__(self, codice, nominativo, livello)
        self.reparto = reparto
        self.capoReparto = capoReparto
        
    def __str__(self):
        a = "\nCodice: " + str(self.codice)
        b = "\nNominativo: " + str(self.nominativo)
        c = "\nLivello: " + str(self.livello)
        d = "\nReparto: " + str(self.reparto)
        e = "\nCaporeparto: " + str(self.capoReparto)
        
        return a + b + c + d + e
    
class Impiegato(Lavoratore):
    def __init__(self, codice, nominativo, livello, mansione):
        Lavoratore.__init__(self, codice, nominativo, livello)
        self.mansione = mansione
        
    def __str__(self):
        a = "\nCodice: " + str(self.codice)
        b = "\nNominativo: " + str(self.nominativo)
        c = "\nLivello: " + str(self.livello)
        d = "\nMansione: " + str(self.mansione)
        
        return a + b + c + d

class Dirigente(Impiegato):
    def __init__(self, codice, nominativo, mansione, nazione):
        # super().__init__(...)
        Impiegato.__init__(self, codice, nominativo, 10, mansione)
        self.nazione = nazione
        
    def __str__(self):
        a = "\nCodice: " + str(self.codice)
        b = "\nNominativo: " + str(self.nominativo)
        c = "\nLivello: " + str(self.livello)
        d = "\nMansione: " + str(self.mansione)
        e = "\nNazione: " + str(self.nazione)
        
        return a + b + c + d + e
        

# main

mario = Lavoratore(112, "Mario", 4)
print(mario)

luigi = Operaio(114, "Luigi", 3, "vernici", "Bowser")
print(luigi)

ayri = Impiegato(116, "Ayri", 2, 300)
print(ayri)

m = Dirigente(118, "m", 400, "svezia")
print(m)
