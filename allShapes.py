from turtle import Turtle, Screen
import random

pencil = Turtle()
colors = ["red", "green", "blue", "yellow", "orange", "purple", "cyan", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

numberOfSides = 10
pencil.speed(1)


def draw_shape(numberOfSides):
	angle = 360 / numberOfSides
	for _ in range(numberOfSides):

		pencil.forward(100)
		pencil.right(angle)


for n in range(3, 11):
	pencil.color(random.choice(colors))
	draw_shape(n)



















my_screen = Screen()
my_screen.exitonclick()
