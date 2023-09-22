# Leandro Gridelli

frase = "Il computer impazzito di '2001 odissea nella spazio' si chiamava HAL"

start = frase.find("'")
end = frase.find("'", start+1)
estratto = frase[start:end]

print(estratto.strip("'").upper())