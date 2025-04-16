"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=640, height=360)# Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 


colors = [ 'red', 'blue', 'pink', 'orange']    # define a list of colors
tina.pensize(15)

for color in colors:                            # loop through the colors
    tina.pencolor(color)
    tina.forward(50)
    tina.left(90)

tina.penup()
tina.left(180)
tina.forward(100)
tina.pendown()

# 2) Make another square, but put the colors in reverse order, using a negative index.
length = len(colors)
for i in range(length):
    tina.pencolor(colors[length - 1 - i])
    tina.forward(100)
    tina.left(90) #set to 90 later







turtle.exitonclick()                     # Close the window when we click on it