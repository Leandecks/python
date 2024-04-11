# Leandro Gridelli

'''
Fe39 mode
Scrivere una funzione con relativa docstring che, acquisita in input una lista di numeri, restituisca la
moda(nel caso siano presenti piu mode la funzione deve comportarsi nel sequente modo:
- per un numero di mode è inferiore o uguale a 3 le restituisce tutte inserendole in una lista,
- se il numero di mode supera 3 deve restiture la stringa 'plurimodale'
'''

def mode(lista):
    
    """
    (lista) -> Optional[list, str, int]

    Se c'è una moda sola la restituisce.
    Se ci sono da 1 a 3 mode le restituisce sotto forma di lista
    Se ci sono più di 3 mode restituisce la stringa "plurimodale"
    """
    
    max = 0
    moda = 0
    mode = []
    
    for k in lista:
        if lista.count(k) > max:
            max = lista.count(k)
            moda = k
    
    for k in lista:
        if lista.count(k) == max and k not in mode:
            mode.append(k)
    
    if len(mode) == 1:
        return moda
    elif len(mode) <= 3:
        return mode
    else:
        return "plurimodale"


# main

l = [1,2,3,3,5,5,12,12,34,34]
print(mode(l))
print(help(mode))
