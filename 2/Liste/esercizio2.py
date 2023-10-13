# Leandro Gridelli

'''
Lo script funziona come calcolatrice:
somma(), somma numeri
moltiplica(), moltiplica numeri
differenza(), sottrae numeri
dividi(), divide numeri
'''

def somma(*numeri):
   somma = 0
   for k in numeri:
      somma += k
   return somma

def moltiplica(*numeri):
   prodotto = 1
   for k in numeri:
      prodotto *= k
   return prodotto

def differenza(*numeri):
   diff = numeri[0]
   for k in range(1,len(numeri)):
      diff -= numeri[k]
   return diff

def dividi(*numeri):
   quoziente = numeri[0]
   for k in range(1,len(numeri)):
      quoziente //= numeri[k]
   return quoziente
