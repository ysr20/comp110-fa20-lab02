"""
Module: draw_pentagon

Program to draw a pentagon using turtles.
"""

import turtle

# create a turtle and set the pen color
sat = turtle.Turtle()
sat.color(input("Enter a color to use for the pen: "))
#asks user to enter a length for the sides of the pentagon
go_forward=int(input("Enter a length for the pentagon: "))
# draw the pentagon
sat.forward(go_forward)
sat.left(72)
sat.forward(go_forward)
sat.left(72)
sat.forward(go_forward)
sat.left(72)
sat.forward(go_forward)
sat.left(72)
sat.forward(go_forward)
sat.left(72)
# keep the turtle window open until we click on it
turtle_window = turtle.Screen()
turtle_window.exitonclick()