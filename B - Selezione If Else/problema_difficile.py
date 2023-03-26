# Problema di Leandro Gridelli
'''
Inserire in INPUT il proprio nome.
Il programma calcolerà il seguente codice speciale.
Se è lungo 1, 2 o 3 lettere il codice sarà
Il nome ordinato secondo l’ordine ASCII seguito dalla lettera x se il nome è lungo 1 lettera, seguito dalla lettera y se il nome è lungo 2 lettere e dalla lettera z se il nome è di 3 lettere. Il codice finale sarà in MAIUSCOLO
Se il nome è lungo da 3 a 10 lettere il codice sarà:
Scritto al contrario a passi di 2, con l’aggiunta della lettera f se la lunghezza del nome di partenza è pari, con l’aggiunta della lettera q se la lunghezza iniziale è divisibile per 3 e con l’aggiunta della lettera L (maiuscola) se la lunghezza iniziale non è divisible né per 2 né per 3. Infine il codice sarà scritto con la prima lettera maiuscola
Se il nome sarà lungo più di 10 lettere il codice sarà:
Formato dalle prime tre lettere seguendo l’ordine ASCII dei caratteri. Il codice finale sarà tutto minuscolo
Previeni la situazione che l’utente inserisca degli spazi nel nome, cancellandoli
'''

nome = input("Inserisci il tuo nome: ")

lun = len(nome)

if lun <= 3 and >= 1:
    
