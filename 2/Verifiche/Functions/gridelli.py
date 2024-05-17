# Gridelli Leandro ML07

# La nebbia agli irti COLLI

def estrai_vocali(stringa):
    voc = []
    for k in stringa.lower():
        if k in "aeiou" and k not in voc:
            voc.append(k)
    return sorted(voc)

def estrai_consonanti(stringa):
    cons = []
    for k in stringa.lower():
        if k in "bcdfghlmnpqrstvz" and k not in cons:
            cons.append(k)
    return sorted(cons)
        
def combina(consonanti, vocali):
    stringa = ""
    stringhe = []
    
    for k in range(18):
        k_cons = k
        k_voc = k
        
        if k > len(consonanti) - 1:
            k_cons = k % len(consonanti)
        if k > len(vocali) - 1:
            k_voc = k % len(vocali)
        
        stringa += consonanti[k_cons]
        stringa += vocali[k_voc]
            
    stringhe.append(stringa[:6])
    stringhe.append(stringa[6:12])
    stringhe.append(stringa[12:18])
    stringhe.append(stringa[18:24])
    stringhe.append(stringa[24:30])
    stringhe.append(stringa[30:36])
    
    print("--- risultato  dell'elaborazione richiesta ---")
    for k in stringhe:
        print(k)

# Main

frase = ""
while estrai_vocali(frase) == [] or estrai_consonanti(frase) == []:
    if frase != "":
        print(f"Lista vocali immesse:  {estrai_vocali(frase)}")
        print(f"Lista consonanti immesse:  {estrai_consonanti(frase)}")
        print("Devi immettere nuovamente la frase perchè un elenco è vuoto")
    frase = input("Immetti frase: ")

combina(estrai_consonanti(frase), estrai_vocali(frase))
