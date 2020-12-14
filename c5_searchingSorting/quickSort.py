def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:  # Base Case, it will stop recurring when lenght is 1.

        # This will return the index of the pivot value.
        splitPoint = partition(alist, first, last)

        # This will apply the recursion to both sides once the pivot value is
        # exchanged with the split point.
        quickSortHelper(alist, first, splitPoint - 1)
        quickSortHelper(alist, splitPoint + 1, last)


def partition(alist, first, last):
    pivotValue = alist[first]
    leftMark = first + 1
    rightMark = last

    done = False

    while not done:

        # Stop if left mark reaches right mark.
        while leftMark <= rightMark and alist[leftMark] <= pivotValue:
            leftMark += 1
        while alist[rightMark] >= pivotValue and rightMark >= leftMark:
            rightMark -= 1
        if rightMark < leftMark:  # Left Mark is pivot Value index here.
            done = True
        else:
            alist[leftMark], alist[rightMark] = alist[rightMark], alist[leftMark]
    # Exchange pivot index with split point / right Mark.
    alist[rightMark], alist[first] = alist[first], alist[rightMark]
    # Return split point.
    return rightMark


"""
myList = [random.randint(0, 10_000_000_000) for x in range(100)]
quickSort(myList)
print(myList)
"""

"""
Quick Sort uses divide and conquer strategy. It uses something called pivot
value. This is usually the first value on the list. It then starts comparing
each value with this pivot value, from the left and right. It will exchanges
largest value with smaller. The smaller values remain at the left, the largest
values remain at the right. It stops when all items have been checked. The
pivot value is exchanged in its correct position, and now recursively apply the
same algorithm to the sublists. It stops when the sublists are of size 0 or 1.

There will be log n in base 2 operations to reduce the sublists. For each level,
n comparisons are performed in total. This means a time complexity of O(nlogn).
For best and average case this will be true. However, in the worst case, split
point will always be at the beginning. Which means there will be n layers, each
layer performs (n - 1) comparison less than the previous layer. From (n-1) to 1. 
This is equal to (n-1)(n)/2 which is equal to O(n^2) in the worst case. 
For instance, if the list is already sorted.
"""