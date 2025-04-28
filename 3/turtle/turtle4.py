# Leandro Gridelli

import turtle

def forma(t, l, a):
    t.forward(l)
    for k in range(3):
        t.right(a)
        t.forward(3 * l)
        t.right(a)
        t.forward(l)
        t.right(a)
        t.forward(l)
    
    t.right(a)
    t.forward(3 * l)
    t.right(a)
    t.forward(l)
    
# main

x = 100
ang = 90

turtle.Turtle()
turtle.color("green", "yellow")
turtle.speed(0)
turtle.begin_fill()

forma(turtle, x, ang)

turtle.end_fill()
turtle.done()

