# Leandro Gridelli

''' fino a 10kwh paga 1 euro per kwh
da 10 a 30 incluso paga 1.50 per kwh
da 30 a 100 inculso paga 2 euro per kwh
oltre 100 paga 4 euro per kwh

consumo: 120
pagare:
primi 10 pago 1 tot 10
per i 20 (10-30) pago 1.50 pago tot 30
per i 70 (31-100) pago 2 , tot 140
per 20 che superano cento pago 4, tot 80
TOT: 260
'''

consumo = int(input("Inserisci il consumo in kwh: "))
pagare = 0

if consumo <= 10:
    pagare = consumo
elif consumo > 10 and consumo <= 30:
    pagare = 10 + (consumo-10) * 1.5
elif consumo > 30 and consumo <= 100:
    pagare = 40 + (consumo-30) * 2
elif consumo > 100:
    pagare = 180 + (consumo-100) * 4
else:
    print("C'è qualcosa che non va")

print(f"Con il tuo consumo di {consumo} kwh spendi {pagare} €")
