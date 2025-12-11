# Leandro Gridelli

class ContoCorrente(object):
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo
        
    def __str__(self):
        return f"Il numero del conto è {self.numero}, il saldo è {self.saldo}"
    
    def deposito(self, val):
        self.saldo += val
    
    def prelievo(self, val):
        if self.saldo - val < 0:
            print("Impossibile")
        else:
            self.saldo -= val
            
    def tasso(self, tas):
        self.saldo -= self.saldo * (tas / 100)
