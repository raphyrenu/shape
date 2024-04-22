import turtle
from turtle import Turtle, Screen
import random

pencil = Turtle()
pencil.speed(20)
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color



def drew(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        pencil.color(random_color())
        pencil.circle(100)
        pencil.setheading(pencil.heading() + size_of_gap)


drew(30)































MyScreen = Screen()
MyScreen.exitonclick()
