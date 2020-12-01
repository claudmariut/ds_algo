# Draw Hilbert Curve using turtle module and recursion.
import turtle

h = turtle.Turtle()
wn = turtle.Screen()


def hilbert(level, lenSide, angle):
    # Input Parameters are numeric
    # Return Value: None
    if level == 0:
        return

    h.right(angle)

    hilbert(level - 1, lenSide, -angle)

    h.forward(lenSide)
    h.left(angle)

    hilbert(level - 1, lenSide, angle)

    h.forward(lenSide)

    hilbert(level - 1, lenSide, angle)

    h.left(angle)
    h.forward(lenSide)

    hilbert(level - 1, lenSide, -angle)

    h.right(angle)


size = 600
h.penup()
h.goto(-size / 2.0, size / 2.0)
h.pendown()
h.pensize(3)
wn.tracer(2)
wn.colormode(255)
wn.bgcolor((204, 230, 255))
# For positioning turtle
size = 600
level = 6
lenSide = size / ((2 ** level) - 1)
hilbert(level, lenSide, 90)
wn.exitonclick()