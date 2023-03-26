# Leandro Gridelli

nome = input("Nome: ")
cognome = input("Cognome: ")
ora_ingresso = int(input("Ora di ingresso: "))
minuto_ingresso = int(input("Minuto di ingresso: "))
ora_uscita = int(input("Ora di uscita: "))
minuto_uscita = int(input("Minuto di uscita: "))

codice = cognome[:3] + nome[::2]

tempo_totale = (ora_uscita*60 + minuto_uscita) - (ora_ingresso*60 + minuto_ingresso) # in minuti

tariffa_totale = tempo_totale * 3
tariffa_euro = tariffa_totale // 100
tariffa_cent = tariffa_totale % 100

print(f"\nCodice: {codice.upper()}")
print(f"Importo da pagare: {tariffa_euro},{round(tariffa_cent,2)} €")