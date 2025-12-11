# Leandro Gridelli

class Operaio(object):
    def __init__(self, nome, matricola, mansione):
        self.nome = nome
        self.matricola = matricola
        self.mansione = mansione
        
    def salario(self, ore, tariffa):
        return ore * tariffa
    
class OperaioSpecializzato(object):
    def __init__(self, nome, matricola, mansione):
        Operaio.__init__(self, nome, matricola, mansione)
        
    def salario(self, ore, tariffa):
        return 10 + ore * tariffa

# main

op = Operaio("juri", 12, "artigiano")
print(op.salario(1, 2))

op2 = OperaioSpecializzato("juri2", 143, "cartongesso")
print(op2.salario(3, 4))
