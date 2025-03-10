# Leandro Gridelli

def fact(n):
    f = 1
    for k in range(1, n + 1):
        f *= k
    return f

# main

while True:
    n = int(input("Inserire un numero positivo: "))
    if n > 0:
        break
    
print(f"Il fattoriale di {n} è {fact(n)}")
