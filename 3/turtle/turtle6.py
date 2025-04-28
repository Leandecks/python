# Leandro Gridelli

import turtle


def forma(t, l, a):
    for k in range(38):
        t.right(a)
        t.forward(l)

        a += 0.25
        l -= 2

# main

x = 75
ang = 20

turtle.Turtle()
turtle.speed(3)

forma(turtle, x, ang)

turtle.done()
