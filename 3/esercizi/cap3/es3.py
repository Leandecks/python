# Leandro Gridelli

def vettore(n):
    v = []
    for k in range(n):
        v.append(0)
    return v

a = [1, 2, 3, 4, 5]
v = 0

for i in range(4, -1, -1):
    a[i] = a[i]
    v = a[i]
    print(i, v)
    
print(a)
