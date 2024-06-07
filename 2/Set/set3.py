# Leandro Gridelli

l = [1, 2, 3]
l[1] = 100  # mutable -> not possible key for dict

s = {1, 2, 3}
s.remove(2)  # mutable -> not possible key for dict

s = frozenset(s)  # not mutable anymore -> possible key for dict
# s.add(4) ERROR
