# Leandro Gridelli

parola = input("Immetti una parola: ").lower() 

n=0
v=0

vocali="aeiou"

for lettera in parola:
    if lettera in vocali:
        v+=1

c = len(parola) - v

print(f"La parola ha {v} vocali e {c} consonanti")

if c > v:
    print("Ci sono più consonanti di vocali")
elif c==v:
    print("Ci sono lo stesso numero di consonanti e vocali")
else:
    print("Ci sono più vocali di consonanti")
