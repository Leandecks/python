# Leandro Gridelli

import turtle
import random

def alea(t, l, n):
    for k in range(n):
        t.right(random.randint(1, 360))
        t.forward(l)
        
def sposta(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
        
def cerchio(t, r, x, y, colore):
    t.color(colore, colore)
    sposta(t, x, y - r)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

# main

turtle.Turtle()
turtle.tracer(0, 0)
turtle.setup(700, 700, 0, 0)
finestra = turtle.Screen()

finestra.bgcolor("cyan")
finestra.title("Fiorellino")

turtle.dot()
cerchio(turtle, 180, 0, 0, "green")
cerchio(turtle, 120, 0, 0, "yellow")
cerchio(turtle, 60, 0, 0, "red")

turtle.color("black")
turtle.pensize(3)
alea(turtle, 20, 100)

turtle.hideturtle()

turtle.update()
turtle.done()
