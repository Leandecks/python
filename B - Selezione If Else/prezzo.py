# Leandro Gridelli

ore_ingresso = int(input("Inserisci l'ora di entrata: "))
minuti_ingresso = int(input("Inserisci i minuti d'entrata: "))
ore_uscita = int(input("Inserisci l'ora di uscita: "))
minuti_uscita = int(input("Inserisci i minuti di uscita: "))

h = ore_uscita - ore_ingresso
minuti = minuti_uscita - minuti_ingresso

ore = round(h + minuti / 60)

prezzo = 0

if ore <= 2:
    prezzo = 0
else:
    if ore >= 3 and ore <= 5:
        prezzo = (ore-2)*3
    else:
        if ore > 5:
            prezzo = (ore-5)+9
if prezzo > 15:
    prezzo = 15

print(f"Paghi {prezzo} €")
if prezzo == 15:
    print("Hai raggiunto la tariffa giornaliera. Non puoi pagare di più")
