# Leandro Gridelli

def fibonacci(n):
    f = [0, 1]
    
    while True:
        f.append(f[-1] + f[-2])
        if len(f) == n:
            break
        
    return f
        
# main

print(f"I primi 10 numeri della sequenza sono {fibonacci(10)}")
