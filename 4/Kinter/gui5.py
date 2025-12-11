# Leandro Gridelli

import tkinter

def funzione():
    pulsante.configure(text="Ciao " + a.get(), bg="red")

# main

finestra = tkinter.Tk()
finestra.geometry("400x400")

a = tkinter.StringVar()
a.set("bu")

dati = tkinter.Entry(finestra, textvariable=a)
dati.pack()

pulsante = tkinter.Button(finestra, text="Pulsante", command=funzione)
pulsante.pack()

finestra.mainloop()
