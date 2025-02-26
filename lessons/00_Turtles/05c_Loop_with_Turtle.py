
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""

... # Your code here

import turtle
turtle.setup (500,500)
tina = turtle.Turtle()

sides = 10
distance = 100
angle = 360/sides

for i in range(sides):
    tina.forward(distance)
    tina.left(angle)

turtle.exitonclick()