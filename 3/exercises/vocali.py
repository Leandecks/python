# Leandro Gridelli

def novoc(s):
    f = ""
    
    for k in s:
        if k not in "aeiou":
            f += k
            
    return f

def novocR(s):
    if s == "":
        return s
    elif s[0] in "aeiou":
        return novocR(s[1:])
    else:
        return s[0] + novocR(s[1:])

# main

print(novoc("cane"), novocR("arcobaleno"))