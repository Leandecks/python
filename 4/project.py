# Leandro Gridelli

import tkinter

def listaInStringa(lista):
    stringa = ""
    for k in range(len(lista)):
        if len(lista) == 1:
            return lista[0]
        elif k == len(lista) - 1:
            stringa += " e " + lista[k]
        elif k == 0:
            stringa += lista[k]
        else:
            stringa += ", " + lista[k]
    return stringa

def listaContieneLista(lista1, lista2):
    for el in lista1:
        if el not in lista2:
            return False
        
    return True

class Arrampicatore(object):
    def __init__(self, nome, cognome, eta, paese, grado_max, discipline, tecniche):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.paese = paese
        self.grado_max = grado_max
        self.discipline = discipline
        self.tecniche = tecniche
        
    def __str__(self):
        discipline_str = listaInStringa(self.discipline)
        return f"L'arrampicatore {self.nome} {self.cognome} ha {self.eta} anni, del paese {self.paese} con grado massimo {self.grado_max} nelle discipline {discipline_str}."

class Percorso(object):
    def __init__(self, nome, disciplina, grado, tecniche):
        self.nome = nome
        self.disciplina = disciplina
        self.grado = grado
        self.tecniche = tecniche
        self.chiuso = False
        
    def __str__(self):
        tecniche_str = listaInStringa(self.tecniche)
            
        return f"Il percorso {self.nome} di {self.disciplina} ha grado {self.grado} ed utilizza le tecniche {tecniche_str}."
    
    def chiusura(self, arrampicatore):
        # Il percorso è dato per chiuso se l'atleta pratica la disciplina, ha un grado maggiore o uguale a quello del
        # percorso e se ha tutte le tecniche necessarie per completarlo.

        output = ""
        
        output += f"\n\n{arrampicatore.nome.upper()} PU{'ò'.upper()} CHIUDERE IL PERCORSO {self.nome.upper()}?\n"
        
        if self.disciplina in arrampicatore.discipline:
            output += f"{arrampicatore.nome} pratica {self.disciplina}.\n"
            
            if self.grado <= arrampicatore.grado_max:
                output += f"Il grado di {arrampicatore.nome}, {arrampicatore.grado_max}, è maggiore o uguale al grado del percorso, {self.grado}.\n"
                
                if listaContieneLista(self.tecniche, arrampicatore.tecniche):
                    output += f"{arrampicatore.nome} è abile nelle tecniche {listaInStringa(self.tecniche)}.\n"
                    self.chiuso = True
                else:
                    output += f"{arrampicatore.nome} non è abile in tutte le tecniche: {listaInStringa(self.tecniche)}\n."
            else:
                output += f"Il grado di {arrampicatore.nome}, {arrampicatore.grado_max}, è minore del grado del percorso, {self.grado}.\n"
        else:
            output += f"{arrampicatore.nome} non pratica {self.disciplina}.\n"

        if self.chiuso:
            output += f"{arrampicatore.nome} ha chiuso il percorso!\n"
        else:
            output += f"{arrampicatore.nome} non ha chiuso il percorso.\n"

        return output

class Gara(object):
    def __init__(self, blocco1, blocco2, blocco3, blocco4, arrampicatore):
        self.blocco1 = blocco1
        self.blocco2 = blocco2
        self.blocco3 = blocco3
        self.blocco4 = blocco4
        self.arrampicatore = arrampicatore
        
    def __str__(self):
        return f"La gara è formata da 4 blocchi.\n{str(self.blocco1)}\n{str(self.blocco2)}\n{str(self.blocco3)}\n{str(self.blocco4)}"
    
    def risultati(self):
        output = ""
        nr_chiusi = 0
        output += self.blocco1.chiusura(self.arrampicatore)
        if self.blocco1.chiuso:
            nr_chiusi += 1
            
        output += self.blocco2.chiusura(self.arrampicatore)
        if self.blocco2.chiuso:
            nr_chiusi += 1
            
        output += self.blocco3.chiusura(self.arrampicatore)
        if self.blocco3.chiuso:
            nr_chiusi += 1
            
        output += self.blocco4.chiusura(self.arrampicatore)
        if self.blocco4.chiuso:
            nr_chiusi += 1

        finale = f"{self.arrampicatore.nome} ha chiuso {nr_chiusi} blocchi!"
        output += f"\n\n{finale.upper()}"

        return output

def crea_arrampicatore():
    if nome_inserito.get() == "" or eta_inserito.get() == "" or paese_inserito == "" or grado_max_inserito == "" or discipline_inserito == "" or tecniche_inserito == "":
        output_arrampicatore.configure(text="ATTENZIONE! Non hai inserito tutti i dati! Così svolgerai la gara con l'arrampicatore di prova Adam Ondra")
    else:
        discipline = discipline_inserito.get().split(",")
        tecniche = tecniche_inserito.get().split(",")
        arr = Arrampicatore(nome_inserito.get(), cognome_inserito.get(), eta_inserito.get(), paese_inserito.get(), grado_max_inserito.get(), discipline, tecniche)
        output_arrampicatore.configure(text=str(arr))
        gara1.arrampicatore = arr

def print_gara():
    risultati = gara1.risultati()
    display_gara.configure(text=risultati)

# main

BG = "#fefae0"
PRIME = "#181825"

finestra = tkinter.Tk()
finestra.attributes('-fullscreen', True)
finestra.title("Gestione Arrampicata")
finestra["bg"] = BG

titolo = tkinter.Label(None, text="Gestione arrampicatori", font=("Helvetica", 25), padx=20, pady=20, bg=PRIME, fg=BG)
titolo.grid(row=0, column=2)

# inserimento arrampicatore

inserimento_arrampicatore = tkinter.Label(None, text="Inserisci un nuovo arrampicatore nel database:", bg=BG)
inserimento_arrampicatore.grid(row=1, column=1)

# nome

inserimento_nome_titolo = tkinter.Label(None, text="Nome:", bg=BG)
inserimento_nome_titolo.grid(row=2, column=0)

nome_inserito = tkinter.StringVar()

inserimento_nome = tkinter.Entry(None, textvariable=nome_inserito)
inserimento_nome.grid(row=2, column=1)

# cognome

inserimento_cognome_titolo = tkinter.Label(None, text="Cognome:", bg=BG)
inserimento_cognome_titolo.grid(row=3, column=0)

cognome_inserito = tkinter.StringVar()

inserimento_cognome = tkinter.Entry(None, textvariable=cognome_inserito)
inserimento_cognome.grid(row=3, column=1)

# grado_max

inserimento_grado_max_titolo = tkinter.Label(None, text="Grado massimo:", bg=BG)
inserimento_grado_max_titolo.grid(row=4, column=0)

grado_max_inserito = tkinter.StringVar()

inserimento_grado_max = tkinter.Entry(None, textvariable=grado_max_inserito)
inserimento_grado_max.grid(row=4, column=1)

# discipline

inserimento_discipline_titolo = tkinter.Label(None, text="Discipline praticate:", bg=BG)
inserimento_discipline_titolo.grid(row=5, column=0)

discipline_inserito = tkinter.StringVar()

inserimento_discipline = tkinter.Entry(None, textvariable=discipline_inserito)
inserimento_discipline.grid(row=5, column=1)
# tecniche

inserimento_tecniche_titolo = tkinter.Label(None, text="Tecniche in cui è abile:", bg=BG)
inserimento_tecniche_titolo.grid(row=6, column=0)

tecniche_inserito = tkinter.StringVar()

inserimento_tecniche = tkinter.Entry(None, textvariable=tecniche_inserito)
inserimento_tecniche.grid(row=6, column=1)

# paese

inserimento_paese_titolo = tkinter.Label(None, text="Paese:", bg=BG)
inserimento_paese_titolo.grid(row=7, column=0)

paese_inserito = tkinter.StringVar()

inserimento_paese = tkinter.Entry(None, textvariable=paese_inserito)
inserimento_paese.grid(row=7, column=1)

# eta

inserimento_eta_titolo = tkinter.Label(None, text="Età:", bg=BG)
inserimento_eta_titolo.grid(row=8, column=0)

eta_inserito = tkinter.StringVar()

inserimento_eta = tkinter.Entry(None, textvariable=eta_inserito)
inserimento_eta.grid(row=8, column=1)

# invio

conferma_arrampicatore = tkinter.Button(None, text="Conferma", fg=BG, bg=PRIME, command=crea_arrampicatore)
conferma_arrampicatore.grid(row=9, column=1)

# avvertenze

avvertenze = tkinter.Label(None, text="ATTENZIONE! Inserire discipline e tecniche separate da virgole", bg=BG)
avvertenze.grid(row=10, column=1)

avvertenze2 = tkinter.Label(None, text="ATTENZIONE! Se non inserisci nulla, verrà utilizzato in gara l'arrampicatore prova Adam Ondra", bg=BG)
avvertenze2.grid(row=11, column=1)


# print arrampicatore

output_arrampicatore = tkinter.Label(None, text="", bg=BG)
output_arrampicatore.grid(row=12, column=1)

# inizializzazione gara

percorso_g1 = Percorso("M1", "boulder", "6c", ["coordinativo"])
percorso_g2 = Percorso("M2", "boulder", "7b", ["tacche"])
percorso_g3 = Percorso("M3", "boulder", "7a+", ["placca"])
percorso_g4 = Percorso("M4", "boulder", "5b", ["dyno"])

gara1 = Gara(percorso_g1,percorso_g2, percorso_g3, percorso_g4, Arrampicatore("Adam", "Ondra", 40, "Repubblica Ceca", "9c", ["lead", "boulder"], ["dyno", "placca"]))

# display gara

titolo_gara = tkinter.Label(None, text="Gara", font=("Helvetica", 20), fg=BG, bg=PRIME)
titolo_gara.grid(row=1, column=3)

display_gara = tkinter.Label(None, text=str(gara1), bg=BG)
display_gara.grid(row=2, column=3)

conferma_risultati_gara = tkinter.Button(None, text="Scopri i risultati dell'arrampicatore da te inserito!", bg=PRIME, fg=BG, command=print_gara)
conferma_risultati_gara.grid(row=3, column=3)

display_gara = tkinter.Label(None, text="", bg=BG)
display_gara.grid(row=4, column=3)

# mainloop

finestra.mainloop()
