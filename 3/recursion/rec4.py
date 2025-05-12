# Leandro Gridelli

def test(p):
    v = 0
    c = 0

    for k in p:
        if k in "aeiou":
            v += 1
        else:
            c += 1

    return v == c

def uguali(p, v = 0, c = 0):
    if len(p) == 0:
        return v == c
    elif p[0] in "aeiou":
        v += 1
    else:
        c += 1
    return uguali(p[1:], v, c)

# main

print(test("parola"))
