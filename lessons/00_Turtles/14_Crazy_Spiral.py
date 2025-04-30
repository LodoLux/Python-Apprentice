"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""
import turtle

t = turtle.Turtle()

def make_a_shape(t):
    sides = 5
    angle = 360/sides
    for i in range(sides):
        t.forward(100)
        t.left(angle)

num_shapes = 7

for i in range(num_shapes):
    make_a_shape(t)
    t.right(360/num_shapes)

t.hideturtle()
turtle.done()
