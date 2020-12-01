import turtle

k = turtle.Turtle()
wn = turtle.Screen()
wn.setup(width=1200, height=1200)
k.up()
k.left(90)
k.forward(200)
k.right(90)
k.backward(300)
k.down()

def kochFlake(k, sideLen, levels):
    if levels == 0:
        # Only draw at smallest level.
        k.forward(sideLen)
        return
    # Get smaller each level.
    sideLen /= 3
    kochFlake(k, sideLen, levels - 1)
    k.left(60)
    kochFlake(k, sideLen, levels - 1)
    k.right(120)
    kochFlake(k, sideLen, levels - 1)
    k.left(60)
    kochFlake(k, sideLen, levels - 1)



wn.bgcolor("sky blue")
wn.tracer(2)
k.hideturtle()
k.begin_fill()
k.color("black", "white")
for i in range(3):
    kochFlake(k, 600, 6)
    k.right(120)
k.end_fill()
wn.exitonclick()