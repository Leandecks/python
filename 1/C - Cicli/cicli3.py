# Leandro Gridelli

'''
Data una parola immessa da tastiera scrivi un programma che indica se la parola contiene la lettera h

Data una parola immessa da tastiera scrivi un programma che indica quante lettere e sono presenti nella parole
'''

p = input("Imetti una parola: ")

a = 0

for k in p:
    if k == "h":
        print("La parola contiene una h")
        break
    else:
        a+=1

if a==len(p):
    print("La parola non contiene una h")

print(f"Nella parola {p} ci sono {p.count('e')} 'e'")
