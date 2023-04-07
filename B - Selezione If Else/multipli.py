# Leandro Gridelli

''' Dato un numero da 1 a 100
- se è un multiplo di cinque
- se è un multiplo di 7
- se è multiplo di entrambi

es
nr 10 => multiplo di 5
nr 21 => multiplo di 7
    nr 35 => multiplo di entrambi
nr 4 => è privo di interesse
'''

nr = int(input("Immetti un numero (1-100): "))
if nr > 100:
    print("Il numero è troppo alto")
elif nr % 7 == 0 and nr % 5 == 0:
    print("Il numero è multiplo di 5 e 7")
elif nr % 7 == 0:
    print("Il numero è multiplo di 7")
elif nr % 5 == 0:
    print("Il numero è multiplo di 5")
else:
    print("Il numero è privo di interesse")
