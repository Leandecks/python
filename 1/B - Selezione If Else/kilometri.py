# Leandro Gridelli

km = int(input("Kilometri percorsi: "))
consumo = int(input("Quanti km fa la tua auto con un litro di benzina: "))
costo_benzina = float(input("Costo benzina: "))

opz1 = km * 0.35
opz2_euro = km / 100 * 20
opz2_benz = km / 100 * 10
opz2_benz_costo = opz2_benz * costo_benzina
opz2 = opz2_euro + opz2_benz_costo

print(f"Opzione 1: {opz1} €")
print(f"Opzione 2: {opz2} €")

if opz1 > opz2:
    print("La prima opzione è più conveniente")
elif opz2 > opz1:
    print("La seconda opzione è più conveniente")
else:
    print("Entrambe le opzioni sono convenienti")
    
