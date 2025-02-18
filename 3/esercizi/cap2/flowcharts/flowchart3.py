# Leandro Gridelli

som = 0
mas = 0
avg = 0.0
f = 0
c = 0

while c < 5:
    grade = int(input("Input grade: "))
    som += grade
    c += 1
    
    if grade < 50:
        f += 1
    else:
        if grade > 50:
            mas = grade
avg = som / 5
print(avg, mas, f)
