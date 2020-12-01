import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'


class Maze:
    """Represent a Maze using turtle module."""
    def __init__(self, mazeFileName):
        """Initialize internal representation of maze from file."""
        rowsInMaze = 0  # Temporal variables.
        columnsInMaze = 0
        self.mazeList = []
        with open(mazeFileName, 'r') as fileObject:
            for line in fileObject:
                rowList = []  # Each row is going to be added to the maze list.
                col = 0  # Keep track of which col we are.
                for ch in line[:-1]:  # To remove the newline at the end.
                    rowList.append(ch)  # Append char to the rowList.
                    if ch == 'S':
                        """Coordinates of starting point."""
                        self.startRow = rowsInMaze
                        self.startCol = col
                    col += 1  # Each ch we move, we move a column.
                rowsInMaze += 1  # When we are done with the line, count row.
                self.mazeList.append(rowList) # We append the rowList.
                columnsInMaze = len(rowList)  # Number of columns in maze.

        """When done with reading file, create remaining attributes."""
        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.yTranslate = rowsInMaze / 2
        self.t = turtle.Turtle()
        self.t.shape("turtle")  # Shape of the object in the maze.
        self.wn = turtle.Screen()  # Create instance of screen window.
        self.wn.setup(width=1200, height=800)
        self.wn.setworldcoordinates(0, 0, columnsInMaze, rowsInMaze)

    def drawMaze(self):
        """Draw maze in screen."""
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazeList[y][x] == OBSTACLE:
                    self.drawCenteredBox(x, self.rowsInMaze - y, 'tan')
        self.t.color("black", "black")

    def drawCenteredBox(self, x, y, color):
        self.wn.tracer(2)  # If tracer is 0 it wont show changes.
        self.t.up()
        self.t.goto(x, y)
        self.t.color("black", color)
        self.t.setheading(0)  # Set orientation of turtle. (North)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
        self.t.up()
        # Perform a TurtleScreen update. To be used when tracer is turned off.
        self.wn.update()
        self.wn.tracer(1)

    def moveTurtle(self, x, y):
        """Move turtle object to given coordinates on maze."""
        self.t.up()
        # towards() function returns an angle.
        self.t.setheading(self.t.towards(x + .5, (self.rowsInMaze - y) - .5))
        self.t.goto(x + .5, (self.rowsInMaze - y) - .5)

    def dropBreadCrumb(self, color):
        """Leave marks when path is visited, or dead path."""
        if color == "green":
            self.t.color("black", "green")
            self.t.stamp()
            self.t.color("black", "black")
        else:
            self.t.dot(color)

    def updatePosition(self, row, col, val=None):
        """Update internal representation of the maze."""
        if val:  # None when the path is empty or non-visited.
            self.mazeList[row][col] = val  # Update also in maze list.
        self.moveTurtle(col, row)

        if val == PART_OF_PATH:
            color = "green"
        elif val == TRIED:
            color = "black"
        elif val == DEAD_END:
            color = "red"
        else:
            color = None

        if color:
            self.dropBreadCrumb(color)

    def isExit(self, row, col):
        """Check if exit of the maze."""
        return (row == 0 or row == self.rowsInMaze - 1
                or col == 0 or col == self.columnsInMaze - 1)

    def __getitem__(self, idx):
        """Allows to call object with [] brackets. myMaze[row][col]."""
        return self.mazeList[idx]

