# Leandro Gridelli

import turtle

def rettangolo(t, l, a):
    t.begin_fill()
    
    for k in range(2):
        t.forward(l)
        t.left(a)
        t.forward(l * 3)
        t.left(a)
        
    turtle.end_fill()
    
def palo(t, l, a):
    t.forward(l // 2)
    t.pensize(10)
    

    t.right(a)
    t.forward(l * 3)
    
    t.penup()
    t.pensize(1)
    
def sposta(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
def cerchio(t, r, x, y, colore):
    t.color(colore, colore)
    sposta(t, x, y)
    
    t.begin_fill()
    t.circle(r)
    turtle.end_fill()
    
# main

x = 100
ang = 90
ra = 25

turtle.Turtle()
turtle.tracer(0, 0)
turtle.color("black", "black")

rettangolo(turtle, x, ang)
palo(turtle, x, ang)
cerchio(turtle, ra, 25, 75, "green")
cerchio(turtle, ra, 25, 75 * 2, "yellow")
cerchio(turtle, ra, 25, 75 * 3, "red")

turtle.hideturtle()
turtle.update()
turtle.done()
