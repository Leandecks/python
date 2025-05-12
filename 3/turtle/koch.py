import turtle

def koch_n(t, n, l):
    if n == 0:
        t.forward(l)
    else:
        koch_n(t, n - 1, l / 3)
        t.left(60)
        koch_n(t, n - 1, l / 3)
        t.right(120)
        koch_n(t, n - 1, l / 3)
        t.left(60)
        koch_n(t, n - 1, l / 3)
        
# main

turtle.Turtle()
turtle.tracer(0, 0)
turtle.color("blue")

koch_n(turtle, 3, 300)

turtle.update()
turtle.done()
