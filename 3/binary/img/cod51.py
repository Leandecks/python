# Leandro Gridelli

import random
import turtle

rosso = random.randint(0, 255)
verde = random.randint(0, 255)
blu = random.randint(0, 255)
print(f"{rosso} {verde} {blu}")

massimo = max([rosso, verde, blu])

if rosso == verde == blu:
    print("grigio")
elif massimo == rosso:
    print("rosso")
elif massimo == verde:
    print("verde")
else:
    print("blu")

esa_lista = [str(hex(rosso))[2:].zfill(2), str(hex(verde))[2:].zfill(2), str(hex(blu))[2:].zfill(2)]
esa = f"#{esa_lista[0]}{esa_lista[1]}{esa_lista[2]}"

print(esa)

complementare_lista = [255 - rosso, 255 - verde, 255 - blu]
complementare = f"#{str(hex(complementare_lista[0]))[2:].zfill(2)}{str(hex(complementare_lista[1]))[2:].zfill(2)}{str(hex(complementare_lista[2]))[2:].zfill(2)}"
print(complementare_lista)

t = turtle.Turtle()
t.color(esa)
t.shape("turtle")
turtle.Screen().bgcolor(complementare)
