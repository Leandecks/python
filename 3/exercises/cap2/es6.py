# Leandro Gridelli

n1 = int(input("Inserire numero 1: "))
n2 = int(input("Inserire numero 2: "))
n3 = int(input("Inserire numero 3: "))

c = ""
d = ""

if n1 > n2:
    if n2 > n3:
        d = n1, n2, n3
    else:
        if n1 > n3:
            d = n1, n3, n2
        else:
            d = n3, n1, n2
else:
    if n1 > n3:
        d = n2, n1, n3
    else:
        if n2 > n3:
            d = n2, n3, n1
        else:
            d = n3, n2, n1
