import random
import turtle
from turtle import Turtle, Screen
import lxml
pencil = Turtle()
pencil.width(20)
pencil.speed(30)
turtle.colormode(255)


colors = ["red", "green", "blue", "yellow", "orange", "purple", "cyan", "CornflowerBlue", "DarkOrchid", "IndianRed",
		  "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]


for _ in range(2000):
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)

	random_color = (r, g, b)

	pencil.color(random_color)
	pencil.forward(30)
	pencil.setheading(random.choice(direction))
























myScreen = Screen()
myScreen.exitonclick()
