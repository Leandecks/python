# Leandro Gridelli

x = 33
y = x
x = 100

print(x,y)

x = [33,44]
y = x

print(x,y)

x[1] = 4
print(x,y)

import copy

x = [33,44]
y = copy.deepcopy(x)

x[1] = 4
print(x,y)
