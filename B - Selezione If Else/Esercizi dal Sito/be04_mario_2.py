# Leandro Gridelli

nome = input("Inserisci il tuo nome: ")

nome_capitalized = nome.capitalize()

if nome_capitalized=="Mario":
    print("Benvenuto Mario Bross")
elif len(nome_capitalized) > 4:
    print("Ciao Luigi")
else:
    print("Dati insufficienti")

