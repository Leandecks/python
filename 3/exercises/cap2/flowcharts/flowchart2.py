# Leandro Gridelli

ns = 0

while ns <= 0:
    ns = int(input("Numero di scatti: "))
    
if ns <= 30:
    costo = ns * 0.20
else:
    if ns > 100:
        costo = 16.5 + (ns - 100) * 0.10
    else:
        costo = 6 + (ns - 30) * 0.15
        
costo = costo + 2.50
print(costo)
