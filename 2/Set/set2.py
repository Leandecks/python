# Leandro Gridelli


def genera_libreria():
    volte = int(input("Quanti libri vuoi inserire: "))
    libreria = []
    
    for k in range(volte):
        titolo = input("Inserisci il titolo: ")
        autore = input("Inserisci l'autore: ")
        anno = int(input("Inserisci l'anno di pubblicazione: "))
        genere = input("Inserisci il genere: ")
        
        libro = (titolo, autore, anno, genere)
        libreria.append(libro)
        
    return libreria


def genera_dizionario(lib):
    diz = {}
    generi = []
    
    for libro in lib:
        if libro[3] not in generi:
            generi.append(libro[3])
        
    for gen in generi:
        l_gen = set()
        for libro in lib:
            if libro[3] == gen:
                l_gen.add(libro[0])
                
        diz[gen] = l_gen
        
    return diz


def genere_autore(gen, diz, lib):
    titoli = set()
    
    for g in diz:
        if g == gen:
            titoli = diz[g]
            
    autori = set()
    
    for t in titoli:
        for l in lib:
            if l[0] == t:
                autori.add(l[1])
    
    return autori


def anno_autore(anno, lib):
    autori = set()
    
    for l in lib:
        if l[2] == anno:
            autori.add(l[1])
    
    return autori


def genera_diz_generi(lib):
    diz = {}
    autori = set()
    
    for l in lib:
        autori.add(l[1])
        
    for a in autori:
        gen_a = set()
        
        for l in lib:
            if l[1] == a:
                gen_a.add(l[3])
                
        diz[a] = gen_a
        
    return diz


# Main

# 1. Genera libreria (lista)

# libreria = genera_libreria()
libreria = [('La Grande Storia del Tempo', 'Stephen Hawking', 2008, 'Scienza'), ('The Lord Of The Rings', 'J.R.R. Tolkien', 1954, 'Fantasy'), ('Il Mondo di Sofia', 'J. Gaarder', 1990, 'Filosofia'), ('Die Unendliche Geschichte', 'Michael Ende', 1978, 'Fantasy'), ('Favole', 'Esopo', 300, 'Favole')]

print(f"Libreria: {libreria}")
print()

# 2. Genera libreria (dizionario)

dizionario = genera_dizionario(libreria)
print(f"Il dizionario è: {dizionario}")
print()

# 3. Funzione che da autori da genere

genere_scelto = "Fantasy"

autori_g = genere_autore(genere_scelto, dizionario, libreria)
print(f"Gli autori {genere_scelto} sono: {autori_g}")

# 4. Funzione che da autori da anno

anno_scelto = 2008

autori_a = anno_autore(anno_scelto, libreria)
print(f"Gli autori del {anno_scelto} sono: {autori_a}")

# 5. Funzione che da dizionario di autori: generi

print(genera_diz_generi(libreria))

# 6. 
