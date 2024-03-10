# Leandro Gridelli

def auguri():
    print("Auguri di buon natale")
    
def ripeti(n):
    for k in range(n):
        auguri()

# main

volte = int(input("Inserisci il numero di volte: "))
ripeti(volte)