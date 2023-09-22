# Leandro Gridelli

L = int(input("Inserisci il lato del quadrato: "))
R = int(input("Inserisci il raggio della cfr: "))

pL = 4*L
pR = 2*R*3.14

aL = L*L
aR = R*R*3.14

if pL == pR:
    print("I perimetri sono uguali")
elif pL > pR:
    print("Il perimetro del quadrato è maggiore")
else:
    print("Il perimetro del cerchio è maggiore")

if aL == aR:
    print("Le aree sono uguali")
elif aL > aR:
    print("L'area del quadrato è maggiore")
else:
    print("L'area del cerchio è maggiore")