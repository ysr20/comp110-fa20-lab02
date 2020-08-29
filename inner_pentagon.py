"""
Module: draw_pentagon

Program to draw a pentagon using turtles.
"""

import turtle

# create a turtle and set the pen color
sat = turtle.Turtle()
sat.pencolor("red")

# draw the pentagon
sat.forward(50)
sat.left(72)
sat.forward(50)
sat.left(72)
sat.forward(50)
sat.left(72)
sat.forward(50)
sat.left(72)
sat.forward(50)
sat.left(72)
#smaller pentagon
sat.pencolor("green")
sat.penup()
sat.goto (5,5)
sat.pendown()
sat.forward(25)
sat.left(72)
sat.forward(25)
sat.left(72)
sat.forward(25)
sat.left(72)
sat.forward(25)
sat.left(72)
sat.forward(25)
sat.left(72)
# keep the turtle window open until we click on it
turtle_window = turtle.Screen()
turtle_window.exitonclick()
