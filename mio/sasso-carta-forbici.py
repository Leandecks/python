# Leandro Gridelli
# Sasso Carta Forbici

import random

print("Benvenuto a \"Sasso Carta Forbici\"!")
print("Quando tocca a te puoi scegliere [S]asso, [C]arta o [F]orbici")

lancio = "Q"
ai = "Q"

while lancio == ai or riGioca == "Si":
  lancio = input("Tocca a te! Sasso, carta, forbici: ")

  lancio = lancio.upper()

  while lancio != "S" and lancio != "C" and lancio != "F":
    print("Seleziona S o C o F")
    lancio = input("Tira per bene stavolta: ")

  numeroCasuale = random.randint(1,3)

  if numeroCasuale == 1:
    ai = "S"
    print("Sasso!")
  elif numeroCasuale == 2:
    ai = "C"
    print("Carta!")
  else:
    ai = "F"
    print("Forbici!")

  if lancio == ai:
    print("Mannaggia, abbiamo pareggiato")
  elif (
    lancio == "S" and ai == "F" or
    lancio == "C" and ai == "S" or
    lancio == "F" and ai == "C"
      ):
    print("Mi ha sconfitto!!! Come è possibile?!")
  else:
    print("GODO! Vinco sempre tanto...")

  if lancio != ai:
    riGioca = input("Ti va di rigiocare? (Si/No) ")
  if riGioca == "No":
    print("Ok ciao")
    break