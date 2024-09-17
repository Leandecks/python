def doppie(stringa):
    diz_doppie = {}
    for lettera in stringa:
        if stringa.count(lettera) > 1:
            diz_doppie[lettera] = stringa.count(lettera)
    return diz_doppie

def fattoriale(numero):
    fact = 1
    for k in range(1, numero + 1):
        fact *= k
    return fact

def combinazioni(stringa):
    fattoriale_eccessivo = fattoriale(len(stringa))
    lista_quantita_lettera_doppie = list(doppie(stringa).values())
    prodotto_fattoriali_doppie = 1

    for quantita in lista_quantita_lettera_doppie:
        prodotto_fattoriali_doppie *= fattoriale(quantita)

    return round(fattoriale_eccessivo / prodotto_fattoriali_doppie)

print(doppie("tooth"))
print(round(fattoriale(5) / (fattoriale(2) * fattoriale(2)))) # 30
print(fattoriale(len("tooth"))) # 120
print()

print(combinazioni("tooth"))
print(combinazioni("mele"))
print(combinazioni("aaa"))
