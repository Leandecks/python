# Leandro Gridelli

import random

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

print(f"{str(hex(rosso))[2:].zfill(2)}{str(hex(verde))[2:].zfill(2)}{str(hex(blu))[2:].zfill(2)}")
