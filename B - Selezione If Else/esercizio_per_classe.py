# Leandro Gridelli

''' Esercizio:
Crea un esercizio-quiz:
- Il programma saluta l'utente e gli chiede come si chiama
- Lo saluta di nuovo, ora con il suo nome
- Inizio del quiz: DOMANDA 1: Quanto fa 123+123?
- DOMANDA 2: Quanto fa 5**3?
- DOMANDA 3: Quanto fa 10%7
Infine il quiz da i risultati:
- Se 0/3 corrette => voto 4
- Se 1/3 corrette => voto 6
- Se 2/3 corrette => voto 8
- Se 3/3 corrette => voto 10
L'utente saprà se è promosso o bocciato (sufficiente / insufficiente)
'''

print("Ciao!")
nome = input("Come ti chiami? ")
print(f"Ciao {nome}!")

uno = int(input("DOMANDA 1\nQuanto fa 123+123? "))
due = int(input("DOMANDA 2\nQuanto fa 5^3? "))
tre = int(input("DOMANDA 3\nQuanto fa 10%7? "))

print("I tuoi risultati:")
if uno==246 and due==125 and tre==3:
    print("Voto: 10, sei promosso!")
elif (uno==246 and due!=125 and tre!=3) or (uno!=246 and due==125 and tre!=3) or (uno!=246 and due!=125 and tre==3):
    print("Voto: 6, sei promosso!")
elif (uno==246 and due==125) or (uno==246 and tre==3) or (due==125 and tre==3):
    print("Voto: 8, sei promosso!")
elif uno!=246 and due!=125 and tre!=3:
    print("Voto: 4, sei bocciato...")
