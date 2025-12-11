# Leandro Gridelli

import tkinter

def calcola():
    equazione.configure(text=n1.get())

# main

finestra = tkinter.Tk()
finestra.geometry("200x200")
finestra.title = "Equazioni"

labelA = tkinter.Label(None, text = "a: ")
labelA.grid(column = 0, row = 0)

n1 = tkinter.IntVar()

a = tkinter.Entry(None, textvariable = n1)
a.grid(column = 1, row = 0)

labelB = tkinter.Label(None, text = "b: ")
labelB.grid(column = 0, row = 1)

n2 = tkinter.IntVar()

b = tkinter.Entry(None, textvariable = n2)
b.grid(column = 1, row = 1)

btn = tkinter.Button(None, text="Calcola", command=calcola)
btn.grid(column = 0, row = 2)

equazione = tkinter.Label(None)
equazione.grid(column = 1, row = 2)

finestra.mainloop()
