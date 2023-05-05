# Leandro Gridelli

par1 = input("1) Inserisci una parola: ")
par2 = input("2) Inserisci una parola: ")
par3 = input("3) Inserisci una parola: ")

if len(par1) > len(par2) and len(par1) > len(par3):
    print("La prima parola è la piu lunga")
elif len(par2) > len(par3) and len(par2) > len(par1):
    print("La seconda parola è la piu lunga")
elif len(par3) > len(par1) and len(par3) > len(par2):
    print("La terza parola è la piu lunga")
elif len(par1) == len(par2) == len(par3):
    print("Le parole hanno tutte la stessa lunghezza")    
elif (len(par1) == len(par2)) or (len(par2) == len(par3)) or (len(par1) == len(par3)):
    print("Le due parole più lunghe sono di uguale lunghezza")

max1 = max(par1)
max2 = max(par2)
max3 = max(par3)

if max1 > max2 and max1 > max3:
    print("La prima parola ha il carattere ascii più grande:",max1)
