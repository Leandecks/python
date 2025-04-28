# Leandro Gridelli

import turtle
import random

def quadrato(tartaruga, x):
    for k in range(4):
        tartaruga.forward(x)
        tartaruga.right(90)

# main

ugo = turtle.Turtle()
ugo.shape("turtle")
ugo.color("blue")
quadrato(ugo, 60)
