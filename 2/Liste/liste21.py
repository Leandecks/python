# Leandro Gridelli

'''
Input: "Paarola"
Output: "1P2a1r1o1l1a"
'''

stringa = input("Inserisci una stringa: ")

contatore = 1
output = ""

for k in range(1, len(stringa)):
  if stringa[k] == stringa[k-1]:
    contatore += 1
  else:
    output += str(contatore) + stringa[k-1]
    contatore = 1
  
  if k == len(stringa) - 1:
    output += str(contatore) + stringa[k]

print(stringa, output)

# Michele Gonzalez

""" 
stringa = input("Inserisci una stringa: ")

contatore = 1
lettere = ""
stringaNuova = ""

for k in range(len(stringa)):
  if stringa[k] in lettere:
    contatore += 1
    if k == (len(stringa) - 1):
      stringaNuova += str(contatore) + stringa[k]
      break
  else:
    if k == 0:
      lettere = stringa[k]
    else:
      stringaNuova += str(contatore) + stringa[k-1]
      contatore = 1
      lettere = stringa[k]
print(stringa, stringaNuova)
 """