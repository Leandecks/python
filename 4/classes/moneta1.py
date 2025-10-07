# Leandro Gridelli

import moneta

# main

moneta1 = moneta.Moneta("testa")
print(f"La faccia attuale è {moneta1.get()}\n")

for k in range(3):
    print("Lancio della moneta")
    moneta1.lancia()
    print(f"La faccia attuale è {moneta1.get()}\n")
