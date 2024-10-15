# Leandro Gridelli

def to_dec(b):
  b = b.split(".")
  intera = ''.join(reversed(b[0]))
  decimale = b[1]

  contatore = 0
  intera_dec = 0

  for char in intera:
    if char == "1":
      intera_dec += 2 ** contatore
    contatore += 1

  contatore = 1
  decimale_dec = 0

  for char in decimale:
    if char == "1":
      decimale_dec += 1 / (2 ** contatore)
    contatore += 1

  return intera_dec + decimale_dec

# main

print(to_dec(input("Inserisci un numero binario: ")))
