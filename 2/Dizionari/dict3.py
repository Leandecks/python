# Leandro Gridelli

import random

# main

voti = {
   "Mario": [random.randint(20, 100) / 10, random.randint(20, 100) / 10, random.randint(20, 100) / 10, random.randint(20, 100) / 10],
   "Luigi": [random.randint(20, 100) / 10, random.randint(20, 100) / 10, random.randint(20, 100) / 10, random.randint(20, 100) / 10],
   "Boo": [random.randint(20, 100) / 10, random.randint(20, 100) / 10, random.randint(20, 100) / 10, random.randint(20, 100) / 10],
   "Aldo": [random.randint(20, 100) / 10, random.randint(20, 100) / 10, random.randint(20, 100) / 10, random.randint(20, 100) / 10],
}

studente = input("Di quale studente vuoi conoscere i voti? ").capitalize()
voti_studente = str(voti[studente]).strip("[").strip("]")
media = sum(voti[studente]) / len(voti[studente])
sufficienza = f"è sufficiente" if media >= 6 else f"non è sufficiente"

print(f"I voti di {studente} sono: {voti_studente}")
print(f"La media di {studente} è: {media}")
print(f"{studente} {sufficienza}")
