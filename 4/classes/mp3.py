# Leandro Gridelli

class Lettore:
    def __init__(self, nr_pulsanti, brano_attuale, memoria, volume_attuale):
        self.nr_pulsanti = nr_pulsanti
        self.brano_attuale = brano_attuale
        self.memoria = memoria
        self.volume_attuale = volume_attuale

    def accensione(self):
        print(f"\nACCENSIONE\n{self.nr_pulsanti} pulsanti\n'{self.brano_attuale}' è il brano attuale\n{self.memoria} sono i brani in memoria\nIl volume attuale è {self.volume_attuale}")

    def spegnimento(self):
        print("\n\nSPEGNIMENTO")

    def cerca(self, brano):
        for canzone in self.memoria:
            if canzone == brano:
                print(f"\nIl brano {brano} è presente in memoria.")
                return
        print(f"\nIl brano {brano} non è in memoria.")

    def volume(self, se_aumentare, valore):
        print("\nVolume iniziale:", self.volume_attuale)
        if se_aumentare:
            self.volume_attuale += valore
        else:
            self.volume_attuale -= valore
        print("Volume finale:", self.volume_attuale)

# main

lettore1 = Lettore(
    3,
    "Norwegian Wood",
    ["Norwegian Wood", "15 Piani", "Regentage", "Vind"],
    10
)

lettore1.accensione()
lettore1.cerca("15 Piani")
lettore1.cerca("Hey Jude")
lettore1.volume(True, 10)
lettore1.volume(False, 20)
lettore1.spegnimento()
