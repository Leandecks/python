# Leandro Gridelli

budget = int(input("Inserire budget iniziale: "))
amici = int(input("Inserire nr amici: "))
prezzo = int(input("Costo della pizza: "))

print(f"Spesa: {prezzo * amici}\nResto: {budget - (prezzo * amici)}")
