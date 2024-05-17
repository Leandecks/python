# Leandro Gridelli

def format_list(l):
    for e in range(len(l)):        
        print(l[e], end=", ")
        
        
def format_dl(l):
    for e in l:
        print(e)
        
        
def format_dict(d):
    for e in d:
        print(e, d[e], sep=": ")


amici = [
    {'nome':'Mario','tel':'333 4564893','età':24},
    {'nome':'Ugo','tel':'338 6548936','età':14},
    {'nome':'Luigi','tel':'337 5853332','età':15},
    {'nome':'Aldo','tel':'333 4510023','età':14},
    {'nome':'Roberto','tel':'341 8642599','età':19},
    {'nome':'Paola','tel':'341 8642599','età':17},
    {'nome':'Andrea','tel':'341 8642599','età':13}
]

# nomi

nomi = []

for amico in amici:
    nomi.append(amico["nome"])

print("Nomi: ")
format_list(nomi)
print("\n")

# maggiorenni

magg = []

for amico in amici:
    if amico["età"] >= 18:
        magg.append(amico)

print("Maggiorenni: ")
format_dl(magg)
print()

# finiscono in o

end_o = []

for amico in amici:
    if amico["nome"][-1] == "o":
        end_o.append(amico)
for el in end_o:
    del el["età"]

print("Finiscono con la o: ")
format_dl(end_o)
print()

# hanno lo stesso numero

numeri = {}

for amico in amici:
    if amico["tel"] not in numeri:
        numeri[amico["tel"]] = 1
    else:
        numeri[amico["tel"]] += 1

print("Numeri usati n volte: ")
format_dict(numeri)
print()

# compagnie

aziende = {
    "tim": [333,334,335],
    "wind": [336,337,338,339],
    "iliad": [340,341,344,349]
}

amici_az = {}

for amico in amici:
    ami = amico["nome"]
    prime_tre = int(amico["tel"][:3])
    for azi in aziende:
        if prime_tre in aziende[azi]:
            amici_az[ami] = azi
            
print(amici_az)
