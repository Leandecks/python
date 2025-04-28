# Leandro Gridelli

import turtle

def clessidra(t, l, a):
    t.forward(l)
    t.right(a)
    t.forward(2 * l)
    t.left(a)
    t.forward(l)
    t.left(a)
    t.forward(2 * l)
    
# main

x = 100
ang = 120

turtle.Turtle()
turtle.color("red", "blue")
turtle.begin_fill()

clessidra(turtle, x, ang)

turtle.end_fill()
turtle.done()
