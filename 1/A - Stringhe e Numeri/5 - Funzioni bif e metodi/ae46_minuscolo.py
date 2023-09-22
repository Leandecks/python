# Leandro Gridelli

frase = "Il computer impazzito di '2001 odissea nella spazio' si chiamava HAL"

start = frase.find("'")
end = frase.find("'", start+1)
estratto = frase[start:end].strip("'")

hIndex = frase.find("H")
hal = frase[hIndex:].strip()

fraseNuova = frase[:start+1] + estratto.upper() + frase[end:hIndex] + hal.lower()

print(fraseNuova)