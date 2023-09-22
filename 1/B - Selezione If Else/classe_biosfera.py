# Leandro Gridelli

''' Classe?
1D (1d) Ingresso biosfera ore 12
1E ingresso ore 13
altra classe: mi dispiace ma devi rimanere in classe
'''

classe = input("Di quale classe sei?: ")          # .upper().strip()

cl = classe.upper().strip()                               # classe = classe.upper() ma si perde la variabile iniziale. Sovrascrivere

if cl == "1E":                                                   # if classe == "1E" or classe == "1e"
    print("Ingresso alla biosfera alle ore 13")
else:                                                               # else per non fare ulteriori passaggi al programma (NO if)
    if cl == "1D":
        print("Ingresso alla biosfera alle ore 12") 
    else:
        print("Mi dispiace ma devi rimanere in classe")

##    if cl == "1E":
##        print("Ingresso alla biosfera alle ore 13")
##    elif: cl == "1D":
##        print("Ingresso alla biosfera alle ore 12") 
##    else:
##        print("Mi dispiace ma devi rimanere in classe")
