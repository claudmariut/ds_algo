import random


# Binary Search of an ordered list.
def binarySearchIterative(alist, item):
    # Index of first and last element.
    firstIndex = 0
    lastIndex = len(alist) - 1
    found = False

    while firstIndex <= lastIndex and not found:
        midpoint = (firstIndex + lastIndex) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                lastIndex = midpoint - 1
            if item > alist[midpoint]:
                firstIndex = midpoint + 1

    return found

# Time complexity of this approach is n/(2^k) = 1, where k is the number of times
# we divide the remaining list into to parts. n = (2^k), logn = k. O(logn).


def binarySearchSRec(alist, item):
    if len(alist) == 0:
        return False

    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                # Note that slicing takes O(k) time complexity.
                return binarySearchSRec(alist[:midpoint], item)
            else:
                return binarySearchSRec(alist[midpoint + 1:], item)

# Example using recursion and slicing.
# But if we take in account slicing, it would be O(n - 1) or O(n) + O(logn) in
# worst scenario.


# Recursion without slicing.
def binarySearchRecursion(alist, item, firstIndex, lastIndex):
    # Index of first and last element.
    if firstIndex <= lastIndex:
        midpoint = (firstIndex + lastIndex) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearchRecursion(alist, item, firstIndex, midpoint - 1)
            if item > alist[midpoint]:
                return binarySearchRecursion(alist, item, midpoint + 1, lastIndex)
    else:
        return False



