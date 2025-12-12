# Leandro Gridelli

import tkinter

def chiudi():
    finestra.destroy()
    
def chiudi_finestra(evento):
    finestra.destroy()
    
def cambia_etichetta():
    etichetta.configure(text="etichetta\nmodificata\ndal pulsante", fg="purple")
    
def cambia_testo():
    testo = dati.get()
    etichetta.configure(text="\nciao " + testo + "\nbenvenuto sul mio sito\n")

# main

finestra = tkinter.Tk()
finestra.geometry("500x300")
finestra.bind("<KeyPress-Q>", chiudi_finestra)
finestra["bg"] = "#e5e5e5"

pulsante = tkinter.Button(None, text="pulsante giallo", bg="yellow", width=30, height=3, command=cambia_etichetta)
pulsante.grid(column=1, row=1)

etichetta = tkinter.Label(None, text="questa è la mia prima etichetta\n di prova", bg="#e5e5e5", fg="blue")
etichetta.grid(column=0, row=0, columnspan=2)

dati = tkinter.Entry(None, bg="ivory")
dati.grid(column=2, row=2)

pulsante2 = tkinter.Button(None, text="chiudi", bg="red", command=chiudi)
pulsante2.grid(column = 1, row = 3)

pulsante3 = tkinter.Button(None, text="Come ti chiami?", bg="green", width=20, height=2, command=cambia_testo)
pulsante3.grid(column=3, row=0)

finestra.mainloop()
