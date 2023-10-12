# Leandro Gridelli

scuderie = ["Ferrari","Lotus","Mercedes","McLaren"]
a = "casa"

print(scuderie[1])
print(a[1]) # sembrano identiche

print()

scuderie[1] = "Red Bull" # solo per le liste

print(scuderie)

# rip pc
##for k in scuderie:
##   scuderie.append("Lotus")
##   print(scuderie)

scuderie[2:] = ["RedBull","Honda"]
print(scuderie)

scuderie[3:] = []
print(scuderie)

scuderie[2] = "Honda"
print(scuderie)

del scuderie[1]
print(scuderie)

print()

s = ["Ferrari","Lotus","Mercedes","McLaren"]
del s[1:]
print(s)

s = ["Ferrari","Lotus","Mercedes","McLaren"]
s[1] = "Mercedes"
s[1:1] = "H"
print(s)

s[1:1] = "Honda"
print(s)

s[1:1] = ["Honda"] # inserimento vuole []
print(s)
