# Leandro Gridelli

def vettore(n):
    v = []
    for k in range(n):
        v.append(0)
    return v

a = [1, 2, 3, 4, 5]
b = vettore(5)

for k in range(5):
    b[k] = a[k]
    
print(b)
