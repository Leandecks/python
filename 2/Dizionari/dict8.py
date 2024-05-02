# Leandro Gridelli

consegne = {
    'Aldo': [8, 1, 7, 9, 4],
    'Bruno': [2, 8, 12, 7, 3],
    'Carlo': [11, 2, 3, 5, 7],
    'Dario': [5, 3, 7, 12, 9],
}

paga = {}

for uomo in consegne:
    paga_uomo = 0

    for giorno in consegne[uomo]:
        if giorno > 8:
            paga_uomo += 48 + 7 * (giorno - 8)
        else:
            paga_uomo += 6 * giorno

    paga[paga_uomo] = uomo

print(paga)
