# Leandro Gridelli

'''
Fa inserire 2 set all'utente,
calcola la differenza 
'''

insiemi = []

for k in range(2):
    insieme = set()
    
    print(f"Inserisci per set nr {k}")
    
    while True:
        inserimento = input("Inserisci un numero o q: ")
        if inserimento == "q":
            break
        insieme.add(inserimento)
        
    insiemi.append(insieme)
    
    
print(f"Set 0: {insiemi[0]")
print(f"Set 1: {insiemi[1]")
print(insiemi[0].difference(insiemi[1]))
