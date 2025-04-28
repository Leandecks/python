import turtle
import random

# main

turtle.penup()
x = random.randint(-300, 300)
y = random.randint(-300, 300)
turtle.goto(x, y)
turtle.pendown()

turtle.Turtle()
turtle.color("red", "yellow")
turtle.shape("turtle") # circle, square, arrow
turtle.pensize(4)
turtle.speed(3) # 0 - 10
turtle.begin_fill()

for k in range(4):
    turtle.forward(100)
    turtle.right(90)
    
turtle.end_fill()
turtle.done()
