def vettore():
    n = int(input("Inserisci lunghezza: "))
    v = []
    
    for k in range(n):
        v.append(input("Inserisci elemento: "))
        
    return v

def on_vettore(v):
    while True:
        scelta = input("Immetti scelta:\ns - stampare\no - ordinare\nc - cercare\n>> ")
        if scelta == "s":
            print(v)
        elif scelta == "o":
            print(sorted(v))
        elif scelta == "c":
            cerca = input("Elemento da cercare: ")
            if cerca in v:
                print("Presente")
            else:
                print("Assente")
        else:
            continue

# main

vec = vettore()
on_vettore(vec)
