# Leandro Gridelli

import tkinter
import random

def lancio():
    range1 = random.choice([4, 6, 8, 12, 20])
    
    lancio1 = random.randint(1, range1)
    lancio2 = random.randint(1, range1)
    
    somma = lancio1 + lancio2
    
    etichetta.configure(text=f"Il dado ha {range1} facce\nI lanci sono {lancio1} e {lancio2}\nLa somma è {somma}")

# main

finestra = tkinter.Tk()
finestra.geometry("500x300")

pulsante = tkinter.Button(None, text="Lancia dadi", command=lancio)
pulsante.pack()

etichetta = tkinter.Label(None)
etichetta.pack()

finestra.mainloop()
