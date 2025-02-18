# Leandro Gridelli

while True:
    a = int(input("Inserire a: "))
    b = int(input("Inserire b: "))
    if a >= 0 and b >= 0:
        break
    
p = 0

for i in range(1, b + 1):
    p = p + a
    
print(p)
