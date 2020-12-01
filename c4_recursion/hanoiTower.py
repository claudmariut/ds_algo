from Hanoi import Hanoi, Stack, turtle


def moveTower(height, fromPole, toPole, auxPole):
    """Solve Tower of Hanoi problem depending on height."""
    if height == 1:
        moveDisk(fromPole, toPole)
        h.moveDisks(fromPole, toPole)

    else:
        moveTower(height - 1, fromPole, auxPole, toPole)
        moveDisk(fromPole, toPole)
        h.moveDisks(fromPole, toPole)
        moveTower(height - 1, auxPole, toPole, fromPole)


def moveDisk(fromPole, toPole):
    """Print the moves made."""
    print(f"Move from {fromPole} to {toPole}")


h = Hanoi(4)
moveTower(4, "A", "C", "B")
h.wn.exitonclick()

