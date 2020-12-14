import math


def shellSort(alist):
    # Calculate gaps using Hibbard Sequence.
    gapList = [(2**gap)-1 for gap
               in range(1, int(math.log((len(alist)//2)+1, 2)+1))]

    while gapList != []:
        gap = gapList.pop()
        for startPos in range(gap):
            # To each sublist with gap increment.
            insertionSortGap(alist, startPos, gap)


def insertionSortGap(alist, start, gap):
    # Assume fist item is sorted.
    for index in range(start + gap, len(alist), gap):
        tempValue = alist[index]
        pos = index

        while pos > start and alist[pos - gap] > tempValue:
            alist[pos] = alist[pos - gap]
            pos = pos - gap

        alist[pos] = tempValue


"""myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(myList)
print(myList)"""

"""
Shell sort is a sequence of insertion sorts that are done passing sublists.
But the sublists that are passed are not with contiguous elements, instead, 
the items are distant apart from each other. This distance is called "gap".
By performing insertion sort if sublists using gaps, the list becames more 
sorted using less shifts. This gap decreases sequentially unitll it reaches
1, which is a normal insertion sort. This might seem not very efficient, but
it actually works very good if the gap sequence is adequate. It lay between
O(n) and O(n^2). 

In this particular program, we are using the Hibbard sequence. 2^k-1 as gaps.
But the largest gap will be always half of the list or less. This particular
sequence claims to perform about O(3^2).
"""