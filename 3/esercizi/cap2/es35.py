# Leandro Gridelli

##def is_primo(n):
##    if n == 1:
##        return False
##    if n == 2:
##        return True
##    for k in range(2, n - 1):
##        if n % k == 0:
##            return False
##
##    return True
##
##def scomporre(n):
##    fattori = []
##
##    for j in range(1, n - 1):
##        if  n % j == 0:
##            fattori.append(j)
##
##    primi =  []
##
##    for f in fattori:
##        if is_primo(f):
##            primi.append(f)
##
##    return primi
##
##def fattori(n, f):
##    c = n
##    numeri = []
##    while c != 1:
##        for fatt in f:
##            if c % fatt == 0:
##                c = c // fatt
##                numeri.append(fatt)
##                print(c)
##
##    return numeri

def scomporre(n):
    f = []

    for k in range(1, n -1):
        if n % k == 0:
            f.append(k)

    return f
            

# main

n1 = int(input("Inserisci n1: "))
n2 = int(input("Inserisci n2: "))

scom1 = scomporre(n1)
scom2 = scomporre(n2)



##fattori1 = scomporre(n1)
##fattori2 = scomporre(n2)
##
##scom1 = fattori(n1, fattori1)
##scom2 = fattori(n2, fattori2)
##
if sum(scom1) == n2 and sum(scom2) == n1:
    print("Numeri amichevoli")
##
##print(scom1, scom2

coppie = []

for i in range(1, 10000):
    somma = sum(scomporre(i))
    for j in range(1, 10000):
        if j == somma and sum(scomporre(j)) == i and i != j:
            if (i, j) not in coppie and (j, i) not in coppie:
                coppie.append((i, j))

print(coppie)
