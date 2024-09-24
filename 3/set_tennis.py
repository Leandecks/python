# Leandro Gridelli

calcio = set()

for k in range(5):
    persona = input("Inserisci un calciatore: ")
    calcio.add(persona)
    
tennis = set()

for k in range(6):
    persona = input("Inserisci un tennista: ")
    tennis.add(persona)
    
solo_calcio = calcio.difference(tennis)
solo_tennis = tennis.difference(calcio)

print(f"Calciatori: {len(calcio)}")
print(f"Tennisti: {len(tennis)}")
print(f"Fanno solo calcio: {len(solo_calcio)}")
print(f"Fanno solo tennis: {len(solo_tennis)}")
print(f"Totale persone: {len(calcio.union(tennis))}")
print(f"Fanno solo calcio: {len(solo_calcio.union(solo_tennis))}")

open("set_tennis.txt", "w").write(
    str(len(calcio)) + ","
    + str(len(tennis)) + ","
    + str(len(solo_calcio)) + ","
    + str(len(solo_tennis)) + ","
    + str(len(calcio.union(tennis))) + ","
    + str(len(tennis.union(calcio))) + ","
    + str(len(solo_calcio.union(solo_tennis))) + "\n"
)
