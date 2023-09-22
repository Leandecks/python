# Leandro Gridelli

nr1 = int(input("Inserisci il primo numero: "))
nr2 = int(input("Inserisci il secondo numero: "))

if nr1 == 0 or nr2 == 0:
    print("Non è possibile il confronto")

else:
    if (nr1 > 0 and nr2 > 0) or (nr1 < 0 and nr2 < 0):
        print("I numeri sono concordi")
    else:
        print("I numeri sono discordi")