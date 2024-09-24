# Leandro Gridelli

def indice(peso, statura):
    return peso / (statura ** 2)

def descrizione_indice(indice):
    if indice < 16.01:
        return "Grave magrezza"
    elif indice < 17.5:
        return "Sottopeso"
    elif indice < 18.5:
        return "Leggermente sottopeso"
    elif indice < 25.0:
        return "Regolare"
    elif indice < 30.0:
        return "Sovrappeso"
    elif indice < 35.0:
        return "Obesità di I classe (moderata)"
    elif indice < 40.0:
        return "Obesità di II classe (grave)"
    else:
        return "Obesità di III classe (gravissima)"

# main

persone = {}
persone = {('Mario', 'Rossi'): (67, 1.54), ('Maria', 'Celli'): (80, 1.71), ('Ale', 'Crinelli'): (93, 2.03), ('Juri', 'Bartolini'): (190, 1.42)}

# volte = int(input("Inserisci il numero di persone da inserire: "))
# 
# for k in range(volte):
#     print(f"PERSONA {k}")
#     
#     cognome = input("Inserisci il cognome: ")
#     nome = input("Inserisci il nome: ")
#     statura = int(input("Inserisci la statura (in cm): "))
#     peso = int(input("Inserisci il peso (in kg): "))
# 
#     nome_cognome = (nome, cognome)
#     statura_peso = (peso, statura / 100)
#     persone[nome_cognome] = statura_peso
    
print(persone)
for persona in persone:
    print(f"Nome: {persona[0]}")
    print(f"Cognome: {persona[1]}")
    print(f"Peso: {persone[persona][0]}")
    print(f"Statura: {persone[persona][1]}")
    print(f"Indice di massa corporea: {indice(persone[persona][0], persone[persona][1])}")
    print()
