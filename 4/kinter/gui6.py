# Leandro Gridelli

import tkinter

def funzione():
    numero = int(dati.get())
    quad = numero ** 2
    pulsante.configure(text="Quadrato " + str(quad), bg="red")

# main

finestra = tkinter.Tk()
finestra.geometry("400x400")
finestra.title = "quadrato"

dati = tkinter.Entry(finestra)
dati.pack()

pulsante = tkinter.Button(finestra, text="Pulsante", command=funzione)
pulsante.pack()

finestra.mainloop()

