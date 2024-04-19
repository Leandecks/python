# Leandro Gridelli

a = {
    "dog": "cane", # key - value (chiave - valore)
    "sea": "mare", # key: number | str
    "cat": "gatto" # value: number | str | list ...
}

b = ["cane", "mare", "gatto"]


voti = {
    "Mario": [4, 7, 5],
    "Luigi": [6, 8, 9, 9, 6],
    "Boo": [9, 6]
}

print(a["sea"])
print()

for k in voti:
    print(k, voti[k])

print()
print("Boo" in voti)
