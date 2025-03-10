# Leandro Gridelli

l1 = int(input("Inserire lato 1: "))
l2 = int(input("Inserire lato 2: "))
l3 = int(input("Inserire lato 3: "))

if l1 == l2 == l3:
    print("Equilatero")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("Isoscele")
else:
    print("Scaleno")
