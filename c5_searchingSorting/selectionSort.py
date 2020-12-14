def selectionSort(alist):
    # Last index gets smaller each time.
    for lastIndex in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for index in range(1, lastIndex + 1):
            if alist[index] > alist[positionOfMax]:
                positionOfMax = index

        alist[lastIndex], alist[positionOfMax] = alist[positionOfMax], \
                                                 alist[lastIndex]


"""
myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSort(myList)
print(myList)
"""

"""
The first pass will be n-1 comparisons, the second n-2 comparison...etc,
until 1 last comparison. Worst case scenario will be 0(n^2), 
Average case O(n^2), Best case O(n^2), does not matter the case, it will always
have to perform the same number of comparisons. 
However, selection sort performs only n exchanges, which usually makes it
better than bubble sort on benchmark studies.
"""
