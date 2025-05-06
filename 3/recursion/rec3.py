# Leandro Gridelli

def compatta(stringa):
    if len(stringa) == 0:
        return ""
    elif stringa[0] == " ":
        return compatta(stringa[1:])
    else:
        return stringa[0] + compatta(stringa[1:])

# main

print(compatta("   asd askjfkh a phdsfasdp i    a sdfiuoh   "))
