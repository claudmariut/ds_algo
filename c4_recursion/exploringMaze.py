from Maze import Maze, turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'


def searchFrom(maze, startRow, startCol):
    """Find path to exit a maze."""
    # Try each of four directions from this point until we find a way out.
    # Check for base cases:
    # 1. We have run into an obstacle, return false.
    if maze[startRow][startCol] == OBSTACLE:
        return False
    # 2. We have found a square that has already been explored
    if maze[startRow][startCol] == TRIED:
        return False
    # 3. Success, an outside edge not occupied by an obstacle
    if maze.isExit(startRow, startCol):
        maze.updatePosition(startRow, startCol, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startCol, TRIED)

    # Otherwise, use logical short circuiting to try each direction in turn
    # if needed.
    found = searchFrom(maze, startRow - 1, startCol) or \
            searchFrom(maze, startRow + 1, startCol) or \
            searchFrom(maze, startRow, startCol - 1) or \
            searchFrom(maze, startRow, startCol + 1)

    if found:
        maze.updatePosition(startRow, startCol, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startCol, DEAD_END)
    return found


mazeFile = "text_files/maze.txt"
myMaze = Maze(mazeFile)
myMaze.drawMaze()
# Set turtle object to start point when executing search function.
myMaze.updatePosition(myMaze.startRow, myMaze.startCol)
searchFrom(myMaze, myMaze.startRow, myMaze.startCol)
myMaze.wn.exitonclick()

