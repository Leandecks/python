# Leandro Gridelli

def somme(a, b):
    pari = 0
    dispari = 0
    
    for k in a:
        if k % 2 == 0:
            pari += k
        else:
            dispari += k
    for k in b:
        if k % 2 == 0:
            pari += k
        else:
            dispari += k
            
    return pari, dispari
            

# main

l1 = [1,2,3]
l2 = [4,6,7,3]

print(somme(l1, l2))