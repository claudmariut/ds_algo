def bubbleSort(alist):
    """Return sorted list using bubble Sort."""
    # Limit right side, starting from last index, to index 1 inclusive.
    for subRange in range(len(alist) - 1, 0, -1):
        exchanges = False
        for num in range(subRange):
            if alist[num] > alist[num + 1]:
                alist[num], alist[num + 1] = alist[num + 1], alist[num]
                exchanges = True
        # If no exchange has been made, then list already sorted and break.
        if not exchanges:
            break


"""
myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]

bubbleSort(myList)
print(myList)
"""

"""
The first pass the algorithm makes n-1 comparisons. The second pass n-2, and
so on. The last pass will be 1 comparison. Total comparisons for worst case
= Sequential sum from 1 to n-1. -> [(n-1)(n)]/2 -> n^2/2 - n/2 = O(n^2). 
The average case will be [(n-1)(n)]/4 -> n^2/4 - n/4 = O(n^2).
The best case will be n-1 comparisons -> O(n).
Notice, that this is not taking into account the swapping execution, which
will increase the number of tasks since bubble sort makes a lot of exchanges.
Approximately  n^2/4 - n/4 exchanges on average.
"""

