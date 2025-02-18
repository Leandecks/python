# Leandro Gridelli

n1 = int(input("Inserire numero 1: "))
n2 = int(input("Inserire numero 2: "))
n3 = int(input("Inserire numero 3: "))
n4 = int(input("Inserire numero 4: "))
n5 = int(input("Inserire numero 5: "))

max = 0

for k in [n1, n2, n3, n4, n5]:
    if k > max:
        max = k

print(f"Massimo: {max}")
