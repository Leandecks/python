# Problema di Leandro Gridelli
'''
Inserire in INPUT il proprio nome.
Il programma calcolerà il seguente codice speciale.
- Se è lungo 1, 2 o 3 lettere il codice sarà:
  - Il nome ordinato secondo l’ordine ASCII seguito dalla lettera x se il nome è lungo 1 lettera, seguito dalla lettera y se il nome è lungo 2 lettere e dalla lettera z se il nome è di 3 lettere. Il codice finale sarà in MAIUSCOLO
- Se il nome è lungo da 4 a 10 lettere il codice sarà:
  - Scritto al contrario a passi di 2, con l’aggiunta della lettera f se la lunghezza del nome di partenza è pari, con l’aggiunta della lettera q se la lunghezza iniziale è divisibile per 3 e con l’aggiunta della lettera L (maiuscola) se la lunghezza iniziale non è divisibile né per 2 né per 3. Infine il codice sarà scritto con la prima lettera maiuscola
- Se il nome sarà lungo più di 10 lettere il codice sarà:
  - Formato dalle prime tre lettere seguendo l’ordine ASCII dei caratteri. Il codice finale sarà tutto minuscolo e seguito da "$"

Previeni la situazione che l’utente inserisca degli spazi nel nome, cancellandoli.   

Con l'inserimento di una stringa vuota il programma darà il messaggio: "Come il tuo nome ha 0 lettere?"
'''

n = input("Inserisci il tuo nome: ")
nome = n.strip()
lun = len(nome)

if lun<=3:
    codice = ''.join(sorted(nome))
    if lun == 1:
        codice = (codice + "x").upper()
    elif lun == 2:
        codice = (codice + "y").upper()
    elif lun == 3:
        codice = (codice + "z").upper()
    else:
        print("Come il tuo nome ha 0 lettere?")
elif lun>=4 and lun<=10:
    codice = nome[::-2]
    if lun % 2 == 0:
        codice = (codice + "f").capitalize()
    elif lun % 3 == 0:
        codice = (codice + "q").capitalize()
    else:
        codice = (codice + "L").capitalize()
else:
    codice = ''.join(sorted(nome))[:3] + "$"

print(f"Il tuo codice speciale è {codice}")