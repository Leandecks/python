# Leandro Gridelli

def perfetto(n):
    f = []
    for k in range(1, n):
        if n % k == 0:
            f.append(k)
    return True if sum(f) == n else False

# main

print("Numeri perfetti:\n")

for i in range(1, 10000):
    if perfetto(i):
        print(i)
