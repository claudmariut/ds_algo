def listSum(numList):
    """Return sum of numbers of list using recursion."""
    if len(numList) == 1:  # Base case. Law 1.
        return numList[0]
    else:
        return numList[0] + listSum(numList[1:])  # Recursion. Law 2, 3.


listSum([x for x in range(10)])



