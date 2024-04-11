# Leandro Gridelli

def mediana(lista):

    # lista = sorted(lista)
    #
    # if len(lista) % 2 != 0:
    #     return lista[len(lista) // 2]
    # else:
    #     posizioni_centrali = [len(lista) // 2, len(lista) // 2 - 1]
    #     numeri_centrali = []
    #
    #     for k in range(len(lista)):
    #         if k in posizioni_centrali:
    #             numeri_centrali.append(lista[k])
    #
    #     return sum(numeri_centrali) / 2

    return sorted(lista)[len(lista) // 2] if len(lista) % 2 != 0 else sum(sorted(lista)[k] for k in range(len(sorted(lista))) if k in [len(lista) // 2, len(lista) // 2 - 1]) / 2

# main

l = [2, 5, 1, 7, 9, 8]  # [1,2,3,4,4,5]
print(mediana(l))
