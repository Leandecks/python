# Leandro Gridelli

import turtle


def forma(t, l, a):
    for k in range(5):
        t.right(a)
        t.forward(l)

# main

x = 300
ang = 180 - 36

turtle.Turtle()
turtle.color("green", "yellow")
turtle.speed(0)
turtle.begin_fill()

forma(turtle, x, ang)

turtle.end_fill()
turtle.done()

