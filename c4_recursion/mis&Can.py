"""
In the missionaries and cannibals problem, three missionaries and three
cannibals must cross a river using a boat which can carry at most two people,
under the constraint that, for both banks, if there are missionaries present
on the bank, they cannot be outnumbered by cannibals
"""
import sys
sys.path.append("/home/claumariut/Documents/ds_algo/c3_basicDataStructures")
from Queue1 import Queue
from Stack import Stack


class MissionariesCannibals:
    """To solve problem with three missionaries and cannibals."""

    def __init__(self, m, c, s):
        """Using states (m, c, s), m, c on left side, s (side of boat)"""
        self.states = Stack()
        self.m = m
        self.c = c
        self.s = s
        # Initial state.
        self.init = (m, c, s)
        self.fs = "R" if s == "L" else "L"
        # Target state.
        self.goal = (0, 0, self.fs)
        self.actions = Queue()
        self.actions.items = [(-1, -1, self.fs), (-2, 0, self.fs),
                              (-1, 0, self.fs), (0, -2, self.fs),
                              (0, -1, self.fs), (1, 1, s), (2, 0, self.s),
                              (1, 0, self.s), (0, 2, self.s), (0, 1, self.s)]

        self.solution = Stack()

    def findSolution(self, state, action=None):
        # To handle first call.
        if action == None:
            nextState = state
            self.states.push(nextState)
        else:
            nextState = ((state[0] + action[0], state[1] + action[1], action[2]))
            # Check for dead ends.
            if nextState[0] != 0:
                if nextState[1] > nextState[0]:
                    return False
            if nextState[0] > self.m or nextState[1] > self.m or \
                    state[2] == nextState[2]:
                return False
            if (self.m - nextState[0]) != 0:
                if (self.m - nextState[1]) > (self.m - nextState[0]):
                    return False
            if nextState in self.states.items:
                return False
            # Check for goal state.
            if nextState == self.goal:
                self.states.push(nextState)
                return True
            # Push state into the states stack.
            self.states.push(nextState)

        valid = False
        # Try each possible action in current state.
        for action in self.actions.items:
            valid = self.findSolution(nextState, action)
            if valid:
                # Valid when goal state found. Start stacking solution.
                self.solution.push(action)
                break

        if valid:
            return True

        else:
            # If no action works, remove last state, and return previous call.
            self.states.pop()
            return False

    def displaySolution(self):
        for i in range(mc.solution.size()):
            action = mc.solution.pop()
            boatSide = None
            if action[2] == "R":
                boatSide = "right"
            else:
                boatSide = "left"
            if action[1] != 0 and action[0] != 0:
                print(
                    f"Move {abs(action[0])} m and {abs(action[1])} c to the {boatSide}")
            elif action[0] != 0:
                print(f"Move {abs(action[0])} m to the {boatSide}")
            elif action[1] != 0:
                print(f"Move {abs(action[1])} c to the {boatSide}")


mc = MissionariesCannibals(3, 3, "R")  # m, c, s
mc.findSolution(mc.init)  # Initial state
mc.displaySolution()


"""
An obvious generalization is to vary the number of jealous couples 
(or missionaries and cannibals), the capacity of the boat, or both. If the boat
holds 2 people, then 2 couples require 5 trips; with 4 or more couples, the 
problem has no solution. If the boat can hold 3 people, then up to 5 couples 
can cross; if the boat can hold 4 people, any number of couples can cross. 
A simple graph-theory approach to analyzing and solving these generalizations 
was given by Fraley, Cooke, and Detrick in 1966.
"""
