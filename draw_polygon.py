"""
Module: draw_polygon

Program to draw a regular polygon based on user's input.
"""

import turtle

# create a turtle and set the pen color
duzzy = turtle.Turtle()
duzzy.pencolor("red")
# asks user for the length of the pentagon
go_forward=int(input("Enter a length for the pentagon: "))
#asks user for number of sides in polygon
side_number=int(input("Choose number of sides: "))
#draw polygon
for i in range(side_number):
    duzzy.forward(go_forward)
    duzzy.left(360/side_number)

# keep the turtle window open until we click on it
turtle_window = turtle.Screen()
turtle_window.exitonclick()
