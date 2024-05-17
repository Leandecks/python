# Leandro Gridelli

tupla = (2, 5, 7) # parentesi optional
# print(tupla[1])
# tupla[0] = 3  non modificabile
 
tupla = tupla[0], 99, tupla[2]

# print(tupla)
# 
# piloti = []
# 
# for k in range(4):
#     nome = input("Nome: ")
#     numero = input("Numero: ")
#     auto = input("Auto: ")
# 
#     pilota = nome, numero, auto
# 
#     piloti.append(pilota)
# 
# print(piloti)

piloti = [('Mario', '1', 'Ferrari'), ('Ugo', '99', 'Honda'), ('Luigi', '56', 'Alfa Romeo'), ('Boo', '66', 'Clio')]

x, y, z = piloti[1]
# print(x, y, z)

def quadrato(lato):
    area = lato ** 2
    perimetro = lato * 4
    return area, perimetro

# dato = int(input("Immetti lato: "))
# a, p = quadrato(dato)
# esito = quadrato(dato)
# print(f"Area: {a}; perimetro: {p}")
# print(esito)

# print(divmod(10, 3))

# a = 5
# b = 7
# # appoggio = a
# # a = b
# # b = appoggio
# a, b = b, a
# 
# print(a, b)

# a = 2, 3, 4
# b = 3, 0, 0
# print(a > b)

# a = 2, 3, 4, 5
# for k in a:
#     print(k)

rubrica = {
    ("Bross", "Mario"): 12983019238,
    ("Fantozzi", "Ugo"): 128301923,
    ("Bross", "Luigi"): 127091873079 # lista per key non va
}

nome = input("Immetti nome da cercare: ")
for k in rubrica:
    if k[0] == nome:
        print(k, "\t Tel", rubrica[k])
    else:
        print(f"{nome} non è presente")
