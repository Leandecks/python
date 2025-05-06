# Leandro Gridelli

import turtle

def rombo(t, l, d):
    for k in range(2):
        t.forward(l // 3)
        t.right(30)
        t.forward(l)
        t.right(30)
        t.forward(l // 3)
        t.right(120)
        
    t.right(d)
    
def petali(t, x, l):
    t.penup()
    t.forward(x)
    t.pendown()
    turtle.left(30)
    rombo(turtle, l, 30)
    t.penup()
    t.right(180)
    t.forward(x)
    t.right(180)
    t.pendown()
    t.right(30)
    
def sposta(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
def cerchio(t, r, x, y):
    sposta(t, x, y - r)
    t.circle(r)
    
# main

lato = 75

turtle.Turtle()
turtle.color("blue")
turtle.tracer(0, 0)
# turtle.speed(5)

# turtle.penup()
# turtle.right(90)
# turtle.forward(25)
# turtle.pendown()
# turtle.circle(50)

for k in range(12):
    petali(turtle, 150, lato)


cerchio(turtle, 50, 0, 0)

turtle.update()
turtle.done()
