# Leandro Gridelli

import random


def genera_prezzo():
    return random.randint(10000, 25000)


def genera_km():
    return random.randint(12, 25)


def genera_cilindrata():
    return random.randint(1000, 1600)


def genera_dati():
    return (genera_prezzo(), genera_km(), genera_cilindrata())


def consuma_meno(diz):
    mini = 0
    macchina_min = ""

    for k in diz:
        if diz[k][1] > mini:
            mini = diz[k][1]
            macchina_min = k

    return macchina_min


def maggiore_cilindrata(diz):
    mini = 0
    macchina_cil = ""

    for k in diz:
        if diz[k][2] > mini:
            mini = diz[k][2]
            macchina_cil = k

    return macchina_cil


def piu_costosa(diz):
    mini = 0
    macchina_cos = ""

    for k in diz:
        if diz[k][0] > mini:
            mini = diz[k][0]
            macchina_cos = k

    return macchina_cos


def miglior_rapporto(diz):
    mini = 3000
    macchina_rapp = ""

    for k in diz:
        rapporto = diz[k][0] / diz[k][1]

        if rapporto < mini:
            mini = rapporto
            macchina_rapp = k

    return macchina_rapp


def meno_costose(diz):
    macc = []
    prezzi = []

    for k in diz:
        if diz[k][0] < 15000:
            macc.append(k)
            prezzi.append(diz[k][0])

    prezzi = sorted(prezzi)

    ord = []

    for prezzo in prezzi:
        for k in diz:
            if diz[k][0] == prezzo:
                ord.append(k)

    return ord


def diz_in_file(d, f):
    for k in d:
        f.write(k + ":" + str(d[k][0]) + "," + str(d[k][1]) + "," + str(d[k][2]) + "\n")


# Main

auto = ["Cinquecento", "Mini", "Golf", "Duster", "Panda"]

diz_auto = {}

for a in auto:
    diz_auto[a] = genera_dati()

print(diz_auto)

# 1. Auto che consuma meno

auto_consuma_meno = consuma_meno(diz_auto)

print(f"Auto che consuma meno: {auto_consuma_meno}")

# 2. Auto di maggiore cilindrata

auto_maggiore_cilindrata = maggiore_cilindrata(diz_auto)

print(f"Auto di maggiore cilindrata: {auto_maggiore_cilindrata}")

# 3. Auto più costosa

auto_piu_costosa = piu_costosa(diz_auto)

print(f"Auto più costosa: {auto_piu_costosa}")

# 4. Rapporto prezzo / km più basso

auto_miglior_rapporto = miglior_rapporto(diz_auto)

print(f"Auto con il miglior rapporto prezzo / km: {auto_miglior_rapporto}")

# 5. Prezzo < 15000, lista ordinata

macchine_prezzo_basso = meno_costose(diz_auto)

print(f"Auto con un costo minore di 15000, ordinate in modo decrescente: {macchine_prezzo_basso}")

# 6. Scrivi in Auto.txt

file = open("Auto.txt", "w")
diz_in_file(diz_auto, file)
file.close()

print("Il file Auto.txt è stato scritto\n")

# 7. Scrivere le auto dal file

dati = open("Auto.txt")
diz_dati = {}

for riga in dati:
    riga = riga.strip("\n")
    c, v = riga.split(":")
    v1, v2, v3 = v.split(",")

    diz_dati[c] = (v1, v2, v3)

for chiave in diz_dati:
    print(chiave, end="\t\t")

    for elemento in diz_dati[chiave]:
        print(elemento, end="\t\t")

    print()
