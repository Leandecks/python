# Leandro Gridelli

media = 0
massimo = 0
minimo = 0

x = int(input("Quanti numeri vuoi: "))

if x != 0:
    n = input("Inserisci numero: ")
    minimo = int(n)

    for k in range(x - 1):
        n = input("Inserisci numero: ")
        if str(n) == "q":
            break
        n = int(n)
        media += n
        if n > massimo:
            massimo = n
        if n < minimo:
            minimo = n

    media = media / x

    print(f"La media è {round(media)}")
    print(f"Il massimo è {massimo}")
    print(f"Il range è {massimo - minimo}")
else:
    print("Non puoi inserire 0 volte")
