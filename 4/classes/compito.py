# Leandro Gridelli

class Personaggio(object):
    pianoDiGioco = [5, 5]
    def __init__(self, nome, posizione, zaino, livelloEnergia):
        self.nome = nome
        self.posizione = posizione
        self.zaino = zaino
        
        while len(self.zaino) > 4:
            print(f"Lo zaino contiene questi elementi: {self.zaino}")
            togliere = input("Quale elemento vuoi togliere? ")
            for k in self.zaino:
                if k == togliere:
                    self.zaino.remove(togliere)
        
        if livelloEnergia > 10:
            self.livelloEnergia = 10
        else:
            self.livelloEnergia = livelloEnergia
            
    def __str__(self):
        return f"{self.nome} si trova in {self.posizione}, con gli item {self.zaino} e un'energia di {self.livelloEnergia}"
    
    def cambiaPosizione(self, x, y):
        if x > Personaggio.pianoDiGioco[0] or y > Personaggio.pianoDiGioco[1]:
            print("Troppo lontano")
        else:
            self.posizione = [x, y]
        
    def passoX(self):
        if self.posizione[0] + 1 > Personaggio.pianoDiGioco[0] or self.posizione[1] > Personaggio.pianoDiGioco[1]:
            print("Troppo lontano")
        else:
            self.posizione[0] += 1
        
    def passoY(self):
        if self.posizione[0] > Personaggio.pianoDiGioco[0] or self.posizione[1] + 1 > Personaggio.pianoDiGioco[1]:
            print("Troppo lontano")
        else:
            self.posizione[1] += 1
        
    def passoDiagonale(self):
        self.passoX()
        self.passoY()
        
    def mettiNelloZaino(self, x):
        if len(self.zaino) < 4:
            self.zaino.append(x)
            
    def togliDalloZaino(self, x):
        if len(self.zaino) == 0 or x not in self.zaino:
            print("Zaino vuoto o elemento non presente")
        else:
            self.zaino.remove(x)
            
    def aumentaEnergia(self):
        self.livelloEnergia += 1
    
    def togliEnergia(self):
        self.livelloEnergia -= 1
            
# main

luigi = Personaggio("Luigi", [1, 2], ["mela", "pera", "banana"], 11)
print(luigi)
luigi.cambiaPosizione(10, 10)
print(luigi)
luigi.passoX()
luigi.passoY()
print(luigi)
luigi.passoDiagonale()
print(luigi)
luigi.mettiNelloZaino("fiore")
print(luigi)
luigi.mettiNelloZaino("fiore2")
print(luigi)
luigi.aumentaEnergia()
print(luigi)
luigi.togliEnergia()
print(luigi)
