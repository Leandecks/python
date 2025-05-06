# Leandro Gridelli

def fatt(n):
    r = 1
    
    for k in range(1, n + 1):
        r *= k
        
    return r

def singoli(stringa):
    if stringa == 0:
        return 1
    else:
        return stringa * singoli(stringa - 1)

# main

print(fatt(0), singoli(4))
