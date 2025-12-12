import tkinter

finestra = tkinter.Tk()
finestra.geometry("1000x800")
finestra.resizable(0, 0)
finestra.title("Test")
finestra["bg"] = "#1010ab"

pulsante = tkinter.Button(None)
pulsante["text"] = "kjshdflkjahskfjahsd"
pulsante["background"] = "#f0f0f0"
pulsante.pack()

pulsante2 = tkinter.Button(None, text = "sdasdasda", bg = "green")
pulsante2.pack()

pulsante3 = tkinter.Button(None, text  = "asdkjashd", bg = "red").pack()

lbl =  tkinter.Label(None, text = "akjslhda", bg =  "lightgreen", fg = "blue")
lbl.pack()

finestra.mainloop()
