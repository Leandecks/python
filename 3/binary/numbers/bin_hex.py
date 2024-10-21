# Leandro Gridelli

def reverse(s):
    return s[::-1]

def to_bin(n):
    b = ""
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            b += "0"
        else:
            n = (n - 1) // 2
            b += "1"
            
    if n == 1:
        return reverse(b + "1")
    else:
        return reverse(b + "0")
            

# main

ins = int(input("Immetti numero: "))
print(to_bin(ins))
