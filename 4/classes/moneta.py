# Leandro Gridelli

import random

class Moneta(object):
    def __init__(self, lato):
        self.lato = lato
        
    def lancia(self):
        if random.randint(0, 1) == 0:
            self.lato = "testa"
        else:
            self.lato = "croce"
            
    def get(self):
        return self.lato
