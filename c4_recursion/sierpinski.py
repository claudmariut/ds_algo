import turtle
from math import sqrt

sTurtle = turtle.Turtle()
myWin = turtle.Screen()
sTurtle.left(90)
sTurtle.up()
sTurtle.backward(300)
sTurtle.down()
sTurtle.left(90)


def drawTriangle(sTurtle, lenSide):
    """Draw triangle."""
    if lenSide < 30:
        sTurtle.color("black", "red")
    elif lenSide < 60:
        sTurtle.color("black", "yellow")
    elif lenSide < 120:
        sTurtle.color("black", "green")
    elif lenSide < 220:
        sTurtle.color("black", "blue")
    elif lenSide < 450:
        sTurtle.color("black", "orange")
    else:
        sTurtle.color("black", "white")

    sTurtle.speed(10)
    sTurtle.begin_fill()
    sTurtle.forward(lenSide/2)
    sTurtle.right(120)
    sTurtle.forward(lenSide)
    sTurtle.right(120)
    sTurtle.forward(lenSide)
    sTurtle.right(120)
    sTurtle.forward(lenSide/2)
    sTurtle.end_fill()
    sTurtle.speed(10)


def sierpinski(sTurtle, lenSide):
    """Get position from were to draw new triangles."""
    if lenSide > 20:
        # Draw a triangle. From coordenates given.
        drawTriangle(sTurtle, lenSide)

        # Find three starting coordinates for last triangle drew.
        leftx = sTurtle.xcor() - lenSide / 4
        lefty = sTurtle.ycor()
        upx = sTurtle.xcor()
        upy = sTurtle.ycor() + (sqrt(3) / 2) * (lenSide / 2)
        rightx = sTurtle.xcor() + lenSide / 4
        righty = sTurtle.ycor()

        # Draw left triangle from coordinates.
        sTurtle.up()
        sTurtle.goto(leftx, lefty)
        sTurtle.down()
        sierpinski(sTurtle, lenSide / 2)

        # Draw up triangle from coordinates.
        sTurtle.up()
        sTurtle.goto(upx, upy)
        sTurtle.down()
        sierpinski(sTurtle, lenSide / 2)

        # Draw left triangle from coordinates.
        sTurtle.up()
        sTurtle.goto(rightx, righty)
        sTurtle.down()
        sierpinski(sTurtle, lenSide / 2)


sierpinski(sTurtle, 800)
myWin.exitonclick()



