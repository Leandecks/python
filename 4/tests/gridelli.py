# Leandro Gridelli

class Monetiera(object):
    def __init__(self, m10, m20, m50, m100, m200):
        self.m10 = m10
        self.m20 = m20
        self.m50 = m50
        self.m100 = m100
        self.m200 = m200
        self.resto = 0
        
    def __str__(self):
        stringa = f"La monetiera contiene:\n{self.m10} monete da 10 centesimi\n{self.m20} monete da 20 centesimi\n{self.m50} monete da 50 centesimi\n{self.m100} monete da 1 euro\n{self.m200} monete da 2 euro "
        return stringa
    
    def getm10(self):
        return self.m10
    def getm20(self):
        return self.m20
    def getm50(self):
        return self.m50
    def getm100(self):
        return self.m100
    def getm200(self):
        return self.m200
    
    def prezzo(self, p):
        self.prezzo = p
        print(f"Il prodotto scelto ha un prezzo di {self.prezzo} centesimi\nimmetti monete\n")
        
    def immissione(self, p1, p2, p3, p4, p5):
        self.p10 = p1
        self.p20 = p2
        self.p50 = p3
        self.p100 = p4
        self.p200 = p5
        
        print(f"Hai immesso::\n{self.p10} monete da 10 centesimi\n{self.p20} monete da 20 centesimi\n{self.p50} monete da 50 centesimi\n{self.p100} monete da 1 euro\n{self.p200} monete da 2 euro ")
    
    def importoImmesso(self):
        return self.p10 * 10 + self.p20 * 20 + self.p50 * 50 + self.p100 * 100 + self.p200 * 200
    
    def pagamento(self):
        if self.prezzo > self.importoImmesso():
            print("Le monete immesse non sono sufficienti")
        else:
            self.resto = self.importoImmesso() - self.prezzo
            self.m10 += self.p10
            self.m20 += self.p20
            self.m50 += self.p50
            self.m100 += self.p100
            self.m200 += self.p200
            
    def daiResto(self):
        print("Ecco il resto :")
        while self.resto > 0:
            if self.resto == 0:
                break
            if self.resto - 200 >= 0:
                self.resto -= 200
                self.m200 -= 1
                print("moneta da 2 euro")
            if  self.resto - 100 >= 0:
                self.resto -= 100
                self.m100 -= 1
                print("moneta da 1 euro")
            if self.resto - 50 >= 0:
                self.resto -= 50
                self.m50 -= 1
                print("moneta da 50 centesimi")
            
            if self.resto - 20 >= 0:
                self.resto -= 20
                self.m20 -= 1
                print("moneta da 20 centesimi")
            
            if self.resto - 10 >= 0:
                self.resto -= 10
                self.m10 -= 1
                print("moneta da 10 centesimi")

        
        print("Operazione conclusa\n")
        
            
# main

m = Monetiera(50, 50, 50, 50, 0)
print(m)
m.prezzo(60)
m.immissione(2, 1, 3, 0, 0)
m.pagamento()
print(f"Importo immesso: {m.importoImmesso()}")
print(f"Prezzo {m.prezzo}")
print(f"Deve avere un resto di {m.resto}")
print("Attendere, bevanda in preparazione\n")
print("Aggiornamento della monetiera")
print(m)
m.daiResto()
print(m)
