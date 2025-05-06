# Leandro Gridelli

def m5(lista):
    if len(lista) == 0:
        return []
    elif lista[0] % 5 == 0:
        return m5(lista[1:])
    else:
        return [lista[0]] + m5(lista[1:])
# main

print(m5([1, 2, 7, 5, 125, 6, 10, 255, 9, 8, 120938]))
