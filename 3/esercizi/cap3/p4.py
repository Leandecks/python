# Leandro Gridelli

while True:
    n = int(input("Inserisci n: "))
    if n > 0:
        break
    
A = []

for i in range(0, n):
    A.append(int(input("Inserire valore: ")))
    
print(A)
    
MAX = A[0]

for i in range(1, n):
    if A[i] > MAX:
        MAX = A[i]
        
print(MAX)
