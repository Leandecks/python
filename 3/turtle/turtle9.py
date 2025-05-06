# Leandro Gridelli

import turtle

def rombo(t, l, d):
    t.right(d)
    for k in range(2):
        t.forward(l)
        t.right(30)
        t.forward(l)
        t.right(60 + 90)
        
def petali(t, l, text, bg):
    t.color(text, bg)
    t.begin_fill()
    for k in range(18):
        rombo(t, l, 20)
    t.end_fill()
        
def sposta(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
        
def cerchio(t, r, x, y, text, bg):
    t.color(text, bg)
    sposta(t, x, y - r)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

# main

turtle.Turtle()
turtle.setup(600, 600, 0, 0)
finestra = turtle.Screen()

finestra.bgcolor("cyan")
finestra.title("Fiorellino")

turtle.tracer(0, 0)
# turtle.speed(3)

petali(turtle, 100, "black", "pink")
cerchio(turtle, 50, 0, 0, "black", "orange")

turtle.hideturtle()

turtle.update()
turtle.done()
