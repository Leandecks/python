# Leandro Gridelli

def x(lista):
    somma_3 = 0
    somma_5 = 0
    
    for k in lista:
        if k % 5 == 0:
            somma_5 += k
        if k % 3 == 0:
            somma_3 += k
    
    return True if somma_3 > somma_5 else False

# main

print(x([3,6,5,7,15,4]))