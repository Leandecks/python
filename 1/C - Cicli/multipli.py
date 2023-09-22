# Leandro Gridelli

'''
Il computer riceve 6 nr da tastiera
Quanti sono multipli di 5?
'''

contatore = 0
n=1

while True:
    n = int(input("Inserisci un numero: "))
    contatore+=1
    if n==0:
        break
'''


for k in range(6):
    n = int(input("Inserisci un numero: "))
    if n%5==0:
        contatore+=1

print(contatore)

'''