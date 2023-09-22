# Leandro Gridelli

import random

numero = int(input("Inserisci un numero: "))

if numero%2==1:
   numero = numero+1

vocali = "aeiou"
consonanti = "bcdfglmnpqrstvz"
parola = ''
random_c = ''
random_v = ''

for k in range(numero//2):
   rand_c = random.randint(0,14)
   rand_v = random.randint(0,4)

   random_c += str(rand_c)
   random_v += str(rand_v)

   
   while str(rand_c) in random_c:
      rand_c = random.randint(0,14)

   
   while str(rand_v) in random_v:
      rand_v = random.randint(0,4)
   



   parola += consonanti[rand_c] + vocali[rand_v]
print(parola)

##risultato = ''
##cons = ''
##voc = ''
##
##for k in range(numero):
##   if k%2==0:
##      rand_cons = random.randint(0,(len(consonanti)+1))
##      cons += str(rand_cons)
##      if str(rand_cons) in cons:
##         rand_cons = random.randint(0,(len(consonanti)+1))
##      risultato += consonanti[rand_cons]
##   else:
##      rand_voc = random.randint(0,4)
##      voc += str(rand_voc)
##      if str(rand_voc) in voc:
##         rand_voc = random.randint(0,(len(vocali)+1))
##      risultato += vocali[rand_voc]
##
##print(risultato)




