# Leandro Gridelli

cantina = {
    "Albana": 100,
    "Barbera": 35,
    "Chianti": 57,
    "Amarone": 15
}

m = 0

for vino in cantina:
    if cantina[vino] > m:
        m = cantina[vino]
        massimo = vino
        
print(m, massimo)

print(max(list(cantina.values())))
