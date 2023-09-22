# Leandro Gridelli

stringa = "xxoooooo         CURIE  ooobbbbbb"

print("Abbiamo questa stringa incasinata:",stringa,"\nMiglioriamola!")

curie = stringa.strip("x").strip("b").strip("o").strip().capitalize()
print(curie)