# Leandro Gridelli


def perimetro_quadrato(l):
    perimetro = 4 * l
    print(f"Il perimetro del quadrato di lato {l} è {perimetro}")
    
    
def area_rett(b, h):
    area = b * h
    print(f"L'area del rettangolo di lati {b} e {h} è {area}")
    
    
def perimetro_rett(b, h):
    perimetro = (b + h) * 2
    print(f"Il perimetro del rettangolo di lati {b} e {h} è {perimetro}")


def primo(n):
    is_primo = True
    
    for k in range(2, n):
        if n % k == 0:
            is_primo = False
            break
    
    if is_primo:
        print("Numero primo")
    else:
        print("Non primo")
        
    
# main

lato = int(input("Lato: "))
lato2 = int(input("Lato 2: "))
perimetro_quadrato(lato)
area_rett(lato, lato2)
perimetro_rett(lato, lato2)

for x in range(2, 100):
    print(x, end = " ")
    primo(x)