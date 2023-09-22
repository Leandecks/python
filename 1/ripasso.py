# Ripasso degli argomenti del primo anno scolastico

# Output, Input, Vars

print("Output")

x = input("Input: ")
print("Input:", x)

'''
Operazioni matematiche:
+
-
*
/
// divisione intera
% resto
** potenza
'''

# Var types, basic formatting

num = 1239
nonint = 123.234
string = "Stringa"
boolean = True

print(f"1239: {type(num)}")
print(f"123.234: {type(nonint)}")
print(f"Stringa: {type(string)}")
print(f"True: {type(boolean)}")

'''
Passaggi tra tipi di variabili:
str()
int()
float()
'''

# Slicing

parola = "Parolona"

print("Considero la prima metà:", parola[:len(parola)//2])
print("Considero le lettere dispari, al contrario:", parola[::-2])
print("Considero la parte 'arol':", parola[1:5])

# Rounding up

numero = 12.2039487
arrotonda = round(numero, 3)
print(arrotonda)

# Imports: sqrt, random

import math

n = 64
sqrt = math.sqrt(n)
print(n, "-", int(sqrt))

import random
print(random.randint(1,27))

# Case Methods

par = "pArOLa"
print(par, par.upper(), par.lower(), par.capitalize(), sep=" - ")

# Removing, replacing, finding, counting methods

p = par.capitalize() # Parola

print(p.find("a"))
print(p.index("a"))
print(p.find("x"))
# print(p.index("x"))   RETURNS ERROR

print(p.replace("a","x"))

p = "   parola  "
print(p.strip())

p = par.capitalize()

print(p.count("a"))

# Control Methods

print(p.isalpha(), p.isnumeric(), p.isupper(), p.lower().islower(), p.isspace())

# ASCII: min, max, sort, ord, chr

print(max(p), min(p))
print(''.join(sorted(p)))
print(ord(p[0]), chr(196))



