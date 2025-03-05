
""""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()

tina.shape('turtle')
tina.speed(2)

def draw_polygon(sides):

    angle = 360/sides
    
    tina.penup()
    tina.goto(x=0, y=100)
    tina.pendown()


    for i in range(sides):
        tina.forward(100)
        tina.left(angle)



for i in range(12, 3, -1):
    draw_polygon(i)

turtle.exitonclick()                     # Close the window when we click on it
