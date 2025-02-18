# Leandro Gridelli

def CaricaVettore(n):
    v = []
    for k in range(n):
        v.append(int(input("Inserire valore: ")))
    return v

def Vettore(n):
    v = []
    for k in range(n):
        v.append("")
    return v

# main

while True:
    n = int(input("Inserire n: "))
    if n > 0:
        break

print("Inserire A")
A = CaricaVettore(n)
print("Inserire B")
B = CaricaVettore(n)
C = Vettore(n)

for i in range(n):
    C[i] = A[i] * B[i]
    
print("C:", C)
