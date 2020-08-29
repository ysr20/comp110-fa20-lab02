"""
Module: draw_polygon

Program to draw a regular polygon based on user's input.
"""

import turtle

# create a turtle and set the pen color
duzzy = turtle.Turtle()
duzzy.pencolor("red")

# PUT YOUR NEW CODE HERE
sides_number=input(int("Choose number of sides: "))
sides_length=input(int("Choose length of sides: "))
for i in range(sides_number):
    duzzy.forward(sides_length)
    duzzy.left(72)

# keep the turtle window open until we click on it
turtle_window = turtle.Screen()
turtle_window.exitonclick()
