# Leandro Gridelli

import tkinter

fin = tkinter.Tk()
fin.geometry("300x100")
fin["bg"] = "yellow"

btn = tkinter.Button(None, text = "Bianco", bg = "white")
btn.pack()
btn2 = tkinter.Button(None, text = "Nero", bg = "black", fg = "white")
btn2.pack()

fin.mainloop()
