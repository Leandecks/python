# Leandro Gridelli

# Scrivi un programma che lancia 2 dadi e indica se avete fatto dadi

import random
a = random.randint(1,6)
b = random.randint(1,6)
c = random.randint(1,6)
print("Dado a:",a)
print("Dado b:",b)
print("Dado c:",c)

if a==b==c:
    print("Hai fatto dadi tripli")
else:
    if a==b or b==c or a==c:
        print("Hai fatto dadi doppi")
    else:
        if a!=b and b!=c and a!=c:
            print("I dadi sono diversi")
