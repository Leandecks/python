# Leandro Gridelli

def media(lista):
    return sum(lista) / len(lista)


def cv(lista):
    return max(lista) - min(lista)


# main

a = [1, 2, 4, 1]

print(media(a))
print(cv(a))
