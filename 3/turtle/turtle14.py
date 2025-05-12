# Leandro Gridelli

import turtle

def quadrato(t, x):
    for k in range(4):
        t.forward(x)
        t.left(90)

def rettangolo(t, b, h):
    for k in range(2):
        t.forward(b)
        t.right(90)
        t.forward(h)
        t.right(90)
        
def sposta(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
def triangolo(t, l):
    t.right(30)
    t.forward(l)
    
    for k in range(2):
        t.right(120)
        t.forward(l)
        
def triangolo2(t, l):
    t.right(180)
    t.forward(l)
    
    for k in range(2):
        t.right(120)
        t.forward(l)
        t.right(120)
        t.forward(l)
        
def fronte(t):
    quadrato(t, 100)
    sposta(t, 33, 0)
    rettangolo(t, 33, 15)
    sposta(t, -10, -15)
    rettangolo(t, 120, 40)

    sposta(t, 33, 115)
    rettangolo(t, 33, 15)
    sposta(t, -10, 155)
    rettangolo(t, 120, 40)

    sposta(t, 120, 110)
    triangolo(t, 120)
    
def coda(t):
    dy = 1
    dx = 0
    
    for k in range(8):
        sposta(t, -30 + dy, 10 + dx)
        rettangolo(t, 80 - 2 * dx, 10)
        dy -= 20
        dx += 2
    
    sposta(t, -185, 85)
    triangolo2(t, 75)
        
# main

turtle.Turtle()
turtle.tracer(0, 0)
turtle.color("blue")
turtle.pensize(3)

fronte(turtle)
coda(turtle)

# turtle.hideturtle()
turtle.update()
turtle.done()
