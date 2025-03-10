# Leandro Gridelli

while True:
    n = int(input("Inserire n: "))
    if n > 0:
        break
    
disp = 1
q = 0

for i in range(1, n + 1):
    q = q + disp
    disp = disp + 2
    print(q, disp)

print(q)
