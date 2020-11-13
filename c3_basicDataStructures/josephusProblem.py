from Queue1 import Queue
"""
People are standing in a circle waiting to be executed. Counting begins at a 
specified point in the circle and proceeds around the circle in a specified 
direction. After a specified number of people are skipped, the next person is 
executed. The procedure is repeated with the remaining people, starting with 
the next person, going in the same direction and skipping the same number of 
people, until only one person remains, and is freed.
"""
# Solution for clockwise direction starting on num1 and killing neighbor. 1 skip.
# Formula says. W(n) = 2^a + l, where a is the biggest power of two below n.
# 2l + 1 is the solution and winning sit.
# In binary, for the solution we take the binary number of n. Take the first
# binary number from the front and move it to the end.


def josephusProblem(n_soliders, skipNum=1):
    """Return Winning sit"""
    soldiersQueue = Queue()
    for i in range(1, n_soliders + 1):
        soldiersQueue.enqueue(i)

    while soldiersQueue.size() > 1:
        for i in range(skipNum):
            soldiersQueue.enqueue(soldiersQueue.dequeue())
        soldiersQueue.dequeue()

    return soldiersQueue.dequeue()


"""
print(josephusProblem(41)) // This returns 19.

41 = 2^5 + 9 = 32 + 9
9 = l --> 2l + 1 = solution --> 2(9) + 1 = 19

41 in binary is 101001.
If we take the first number and put it at the end we get 010011 = 19
"""

