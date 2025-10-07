class Vettore:
    
    def __init__(self):
        v = []
        self.v = v

    def vettore(self):
        n = int(input("Inserisci lunghezza: "))
        
        for k in range(n):
            self.v.append(input("Inserisci elemento: "))

    def on_vettore(self):
        while True:
            scelta = input("Immetti scelta:\ns - stampare\no - ordinare\nc - cercare\n>> ")
            if scelta == "s":
                print(self.v)
            elif scelta == "o":
                print(sorted(self.v))
            elif scelta == "c":
                cerca = input("Elemento da cercare: ")
                if cerca in self.v:
                    print("Presente")
                else:
                    print("Assente")
            else:
                continue

# main

vec = Vettore()
vec.vettore()
vec.on_vettore()
