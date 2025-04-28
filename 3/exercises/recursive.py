# Leandro Gridelli

def fatt(n):
    r = 1
    
    for k in range(1, n + 1):
        r *= k
        
    return r

def ricorsivo(n):
    if n == 0:
        return 1
    else:
        return n * ricorsivo(n - 1)

# main

print(fatt(0), ricorsivo(4))
