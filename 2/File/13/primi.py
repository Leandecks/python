# Leandro Gridelli

file = open("numeri_primi.txt","w",encoding="utf-8") # latin-1, utf-16, cp1252...

primi = [2]
i = 2

while i < 100:
    i += 1
    is_primo = False
    
    for primo in primi:
        if i % primo == 0:
            is_primo = False
        else:
            is_primo = True
    
    if is_primo:
        primi.append(i)
            
        
print(primi)
    
file.close()
