# Leandro Gridelli

a=input("Inserisci una parola con 3x caratteri: ")
print("La parola scelta è lunga",len(a),"caratteri")

x=len(a) / 3
pone=int(x*2)

p1=a[:pone]
p2=a[pone:]

print("La prima parte è",p1.upper(),"ed è composta da",len(p1),"caratteri")
print("La seconda parte è",p2.upper(),"ed è composta da",len(p2),"caratteri")

new=p2[::-1]+p1

print("La nuova parola è",new.lower())
