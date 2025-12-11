# Leandro Gridelli

class Libro(object):
    def __init__(self, titolo, autore, prezzo, quantita):
        self.titolo = titolo
        self.autore = autore
        self.prezzo = prezzo
        self.quantita = quantita
    
    def __str__(self):
        return f"Il titolo è {self.titolo}, l'autore è {self.autore}, il prezzo è {self.prezzo}, la quantità è {self.quantita}"
    
    def vendi(self, quantita_venduta):
        self.quantita -= quantita_venduta
        
    def aumenta_scorta(self, quantita_aggiunta):
        self.quantita += quantita_aggiunta

class Negozio(object):
    def __init__(self):
        self.catalogo = []
        
    def aggiungi_libro(self, libro):
        self.catalogo.append(libro)
        
    def cerca_libro_per_titolo(self, titolo):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                return libro
            
    def cerca_libro_per_autore(self, autore):
        for libro in self.catalogo:
            if libro.autore == autore:
                return libro
    
    def vendi_libro(self, titolo, quantita):
        libro = self.cerca_libro_per_titolo(titolo)
        libro.vendi(quantita)
        
    def mostra_catalogo(self):
        for k in self.catalogo:
            print(k)
            
# main

negozio1 = Negozio()
negozio1.aggiungi_libro(Libro("Commedia", "Dante", "100€", 6))
negozio1.aggiungi_libro(Libro("Porco dio", "Crinelli", "400€", 12))
negozio1.aggiungi_libro(Libro("puttana bel", "Maioli", "10€", 1))

print(negozio1.cerca_libro_per_titolo("puttana bel"))

negozio1.vendi_libro("Porco dio", 2)
negozio1.mostra_catalogo()
