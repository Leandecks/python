# Leandro Gridelli

def stampa_diz(diz):
    for k in diz:
        print(f"{k} -> {diz[k]}")


def se_mille(diz):
    for k in diz:
        if int(diz[k]) >= 1000:
            print(f"{k} ({diz[k]})")


# main
macchine = {}

while True:
    marca = input("Inserisci la marca: ")
    if marca == "q":
        print()
        break

    vendite = input("Inserisci le vendite del 2024: ")
    if vendite == "q":
        print()
        break

    macchine[marca] = vendite

print("Macchine 2024:")
stampa_diz(macchine)
print("\nMacchine con più di mille vendite:")
se_mille(macchine)
