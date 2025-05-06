# Leandro Gridelli

import turtle

def sposta(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def quadrato(t, l, x, y):
    sposta(t, x, y)
    
    for k in range(4):
        t.forward(l)
        t.left(90)
        
def rettangolo(t, b, h, x, y):
    sposta(t, x, y)
    
    for k in range(2):
        t.forward(b)
        t.left(90)
        t.forward(h)
        t.left(90)
        
def triangolo(t, l, x, y):
    sposta(t, x, y)
    
    for k in range(3):
        t.forward(l)
        t.left(180 - 60)
        
def finestre(t, f):
    pos_x = -60

    for k in range(5):
        quadrato(t, f, pos_x, 60)
        pos_x += 25
        
    pos_x = -60

    for k in range(5):
        quadrato(t, f, pos_x, 30)
        pos_x += 25
        
def casa(t, b, h, l, f):
    quadrato(t, l, -100, -100)
    rettangolo(t, b, h, -17, -100)
    finestre(t, f)
    triangolo(t, l + 20, -110, 100)
    
def albero(t, b, h, l, x, yr, yt):
    rettangolo(t, b, h, x, yr)

    pos_y = yt

    for k in range(4):
        triangolo(t, l, x - 30, pos_y)
        pos_y += 20

# main

lato = 200
fin = 15
base = 40
altezza = 60

turtle.Turtle()
turtle.tracer(0, 0)

turtle.color("blue")
turtle.pensize(3)

casa(turtle, base - 10, altezza, lato, fin)
albero(turtle, base, altezza, lato // 2, -300, -100, -40)
albero(turtle, base, altezza, lato // 2, 250, -100, -40)

turtle.hideturtle()

turtle.update()
turtle.done()
