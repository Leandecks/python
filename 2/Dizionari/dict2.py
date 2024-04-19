# Leandro Gridelli

def media(lista):
    return round(sum(lista) / len(lista), 1)


# main

voti = {
    "Mario": [4, 7, 5],
    "Luigi": [6, 8, 9, 9, 6],
    "Boo": [9, 6]
}

for k in voti:
    print(k, media(voti[k]))
    