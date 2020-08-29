"""
Module: draw_pentagon

Program to draw a pentagon using turtles.
"""

import turtle

# create a turtle and set the pen color
sat = turtle.Turtle()
turtle_window = turtle.Screen()
sat.color(input("Enter a color to use for the pen: "))
sat_forward=input("Enter a length for the pentagon: ")
forward=int(sat_forward)
# draw the pentagon
forward()
sat.left(72)
forward()
sat.left(72)
forward()
sat.left(72)
forward()
sat.left(72)
forward()
sat.left(72)
# keep the turtle window open until we click on it
turtle_window.exitonclick()