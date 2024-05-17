# Leandro Gridelli

file = open("promessi.txt", encoding="utf-8")
promessi = file.read()

promessi = promessi.lower()
alfa = "abcdefghijklmnopqrstuvwxyz"

lettere = {}

for x in promessi:
    if x in alfa:
        if x not in lettere:
            lettere[x] = 1
        else:
            lettere[x] += 1
            
chiavi = sorted(list(lettere.keys()))
        
for k in chiavi:
    print(k, "=", lettere[k])
    
file.close()