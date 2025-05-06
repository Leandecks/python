# Leandro Gridelli

import turtle

def quadrato(t, x):
    for k in range(4):
        t.forward(x)
        t.right(90)
        
def sposta(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
def rettangolo(t, b, h):
    for k in range(2):
        t.forward(b)
        t.right(90)
        t.forward(h)
        t.right(90)
        
def cerchio(t, r, x, y, colore):
    t.color(colore, colore)
    sposta(c, x, y - r)
    t.circle(r)

# main

ugo = turtle.Turtle()
ugo.speed(0)
ugo.color("green")
quadrato(ugo, 100)

mario = turtle.Turtle()
mario.speed(0)
mario.color("red")
sposta(mario, 100, 100)
quadrato(mario, 50)

c = turtle.Turtle()
c.speed(0)
cerchio(c, 50, 200, 200, "blue")

turtle.Turtle()
sposta(turtle, 200, 200)
turtle.dot()
