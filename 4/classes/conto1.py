# Leandro Gridelli

import conto

# main

nr = int(input("Inserire numero conto: "))
sald = int(input("Inserire saldo: "))

conto1 = conto.ContoCorrente(nr, sald)
print(str(conto1))

stipendio = int(input("Inserire lo stipendio: "))
conto1.deposito(stipendio)
print(str(conto1))

prelievo = int(input("Inserire valore prelievo: "))
conto1.prelievo(stipendio)
print(str(conto1))

tassa = int(input("Inserire la tassa: "))
conto1.tasso(tassa)
print(str(conto1))
