# Leandro Gridelli

'''
Inseriti 10 nr da tastiera, quanti sono multipli di 3 e quanti di 5?
'''

contatore3 = 0
contatore5 = 0

for k in range(10):
    n = int(input("Inserisci numero: "))
    if n%3==0:
        contatore3 += 1
    if n%5==0:
        contatore5 += 1

print(f"Dei 10 numeri, {contatore3} erano multipli di 3")
print(f"Dei 10 numeri, {contatore5} erano multipli di 5")