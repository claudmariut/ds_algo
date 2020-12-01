from turtle import *
import random
import math

myTurtle = Turtle()
myWin = Screen()


def drawSpiral(myTurtle, lineLen):
    """Draw spiral using myTurtle object from Turtle module using recursion."""
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        for x in range(100):
            myTurtle.forward(1)
            myTurtle.right(1)
        drawSpiral(myTurtle, lineLen - 5)


def drawTree(myTurtle, branchLen):
    if branchLen > 5:
        myWin.tracer(2)
        myTurtle.pensize(math.sqrt(branchLen))
        if branchLen < 40:
            myTurtle.color("green")
            myTurtle.forward(branchLen)
            angle = random.randint(15, 45)
            myTurtle.right(angle)
            drawTree(myTurtle, branchLen - 15)
            myTurtle.left(angle * 2)
            drawTree(myTurtle, branchLen - 10)
            myTurtle.right(angle)
            myTurtle.backward(branchLen)
        else:
            myTurtle.color("brown")
            myTurtle.forward(branchLen)
            angle = random.randint(15, 30)
            myTurtle.right(angle)
            drawTree(myTurtle, branchLen - 15)
            myTurtle.left(angle * 2)
            drawTree(myTurtle, branchLen - 15)
            myTurtle.right(angle)
            myTurtle.backward(branchLen)


myTurtle.setheading(90)
myTurtle.up()
myTurtle.hideturtle()
myTurtle.backward(300)
myTurtle.down()
drawTree(myTurtle, 120)
myTurtle.hideturtle()
myWin.exitonclick()



