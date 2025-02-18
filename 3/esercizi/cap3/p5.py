# Leandro Gridelli

def CaricaVettore(n):
    v = []
    for k in range(n):
        v.append(int(input("Inserire valore: ")))
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

PS = 0

for i in range(n):
    PS = PS + (A[i] * B[i])
    
print(PS)
