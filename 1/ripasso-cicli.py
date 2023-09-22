# Ripasso dei Cicli

'''
Ci sono principalmente 3 tipi di cicli
Quelli che girano sulle posizioni e quelli che girano sulle lettere e enumerate che gira su entrambi
'''

# Tipo 1

parola = "macchina"

for k in range(len(parola)):
    print(k)

print("\n\n")

for k in range(10):
    print(k)

print("\n\n")

# Tipo 2

for k in parola:
    print(k)

# Tipo 3: enumerate

print("\n\n")

for k,t in enumerate(parola):
    print(k,t)