# Leandro Gridelli

frase = "Il computer impazzito di '2001 odissea nella spazio' si chiamava HAL"

hIndex = frase.find("H")
hal = frase[hIndex:].strip()

percento = len(hal) / len(frase) * 100
print(str(round(percento,2)) + "%")