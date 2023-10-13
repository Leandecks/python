# Leandro Gridelli

'''
LISTA DELLA SPESA
Scrivi un programma che permette all'utente di inserire la sua lista della spesa.
Gli inserimenti numerici, decimali e vuoti vengono automaticamente ignorati.
Con l'inserimento di "r" l'utente può generare un elemento casuale da una lista predefinita.
'''

import random

lista_spesa = []
spesa_predefinita = ["Banane","Patate","Pasta","Pizza","Noccioline","Carta Igienica","Pane"]

elemento = ""

while elemento != "q":
  elemento = input("Inserisci un elemento per la tua lista della spesa: ")
  if elemento != "q" and elemento != "r" and not elemento.isnumeric() and not elemento.isspace() and not elemento.isdecimal():
    lista_spesa.append(elemento)
  elif elemento == "r":
    numero_random = random.randint(0,len(spesa_predefinita))
    elemento_random = spesa_predefinita[numero_random]
    lista_spesa.append(elemento_random)

print("La tua lista della spesa è:")
for k in lista_spesa:
  print(f"- {k}")