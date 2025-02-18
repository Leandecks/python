# Leandro Gridelli

def fibonacci(n):
    f = [0, 1]
    
    while True:
        f.append(f[-1] + f[-2])
        if len(f) == n:
            break
        
    return f

# main

while True:
    n = int(input("Inserire intero positivo: "))
    if type(n) == int and n > 0:
        break
    
print(f"Elemento in posizione n: {fibonacci(n)[-1]}")
