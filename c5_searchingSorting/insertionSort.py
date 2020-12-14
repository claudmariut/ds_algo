def insertionSort(alist):
    for firstIndex in range(1, len(alist)):
        currentValue = alist[firstIndex]
        pos = firstIndex
        while pos > 0 and alist[pos - 1] > currentValue:
            alist[pos] = alist[pos - 1]
            pos -= 1

        alist[pos] = currentValue

"""
myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSort(myList, 0, len(myList) - 1)
print(myList)
"""

"""
Insertion sort works at exactly the same way as bubble sort, and selection sort
for the worst, and  average cases. O(n^2). However, for the best case, it will
    be O(n), only n comparisons will be made. This algorithm works very good
    because there is no exchange that requires two operations, but only 
    assignations. It will depend on the size of the list and how the values are
    distributed.
"""
