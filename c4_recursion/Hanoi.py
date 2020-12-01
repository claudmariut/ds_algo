import turtle
import sys
sys.path.append("/home/claumariut/Documents/ds_algo/c3_basicDataStructures")
from Stack import Stack


class Hanoi:
    """Represent tower of hanoi game using turtle module."""
    def __init__(self, disks):
        self.disks = disks
        self.wn = turtle.Screen()
        self.rods = turtle.Turtle()
        self.wn.setup(width=1200, height=600)
        self.wn.setworldcoordinates(0, 0, 120, 40)
        self.drawRods()
        self.source = Stack()
        self.target = Stack()
        self.aux = Stack()
        self.drawDisks()
        self.sourceCor = 30
        self.targetCor = 90
        self.auxCor = 60

    def drawRods(self):
        self.wn.tracer(0)
        for x in range(20, 90, 30):
            self.rods.setheading(0)
            self.rods.up()
            self.rods.hideturtle()
            self.rods.goto(x, 10)
            self.rods.pensize(width=4)
            self.rods.down()
            self.rods.forward(20)
            self.rods.backward(10)
            self.rods.left(90)
            self.rods.forward(15)
        self.wn.update()
        self.wn.tracer(1)

    def drawDisks(self):
        """Draw disks and put them in the source stack"""
        disks = self.disks
        colors = ["brown", "orange", "red", "blue", "green"]
        y = 11.5
        size = 8
        while disks > 0:
            disk = turtle.Turtle()
            disk.shape("square")
            if size < 1:
                size = 1
            disk.shapesize(1.5, size)
            disk.color("black", colors.pop())
            disk.up()
            disk.goto(30, y)
            self.source.push(disk)
            y += 2.5
            disks -= 1
            size -= 2

    def moveDisks(self, sourceRod, targetRod):
        """Internal representation, move disk using turtle and stacks."""
        if sourceRod == "A":
            sourceRod = self.source
        elif sourceRod == "B":
            sourceRod = self.aux
        else:
            sourceRod = self.target

        if targetRod == "A":
            targetRod = self.source
            targetCor = self.sourceCor
        elif targetRod == "B":
            targetRod = self.aux
            targetCor = self.auxCor
        else:
            targetRod = self.target
            targetCor = self.targetCor

        disk = sourceRod.pop()
        targetRod.push(disk)
        size = targetRod.size()
        y = 11.5 + (2.5 * (size - 1))
        disk.goto(targetCor, y)



