# Leandro Gridelli

file = open("cod12.txt").readlines()

for k in file:
    if k.count("1") % 2 != 0:
        print(k + "\tBYTE ERRATO")
    else:
        print(k)
