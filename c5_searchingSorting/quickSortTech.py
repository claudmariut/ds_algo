import statistics
import random

"""Different quick sort techniques to study improvements."""
# Partition limit. One way to improve the quick sort is to use an insertion
# sort on lists that have a small length (call it the “partition limit”).
# Why does this make sense? Re-implement the quick sort and use it to sort a
# random list of integers. Perform an analysis using different list sizes for
# the partition limit.


def quickSortInsertion(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if last - first > 6:  # Base Case, will stop if sublist is 18 or less.

        # This will return the index of the pivot value.
        splitPoint = partition(alist, first, last)

        # This will apply the recursion to both sides once the pivot value is
        # exchanged with the split point.
        quickSortHelper(alist, first, splitPoint - 1)
        quickSortHelper(alist, splitPoint + 1, last)

    else:
        insertionSort(alist, first, last)


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


def insertionSort(alist, first, last):
    for firstIndex in range(first + 1, last + 1):
        currentValue = alist[firstIndex]
        pos = firstIndex
        while pos > 0 and alist[pos - 1] > currentValue:
            alist[pos] = alist[pos - 1]
            pos -= 1

        alist[pos] = currentValue


"""
Based on an experiment. Insertion Sort perform better than quick sort on ranges
bellow and including 8 approximately. This is why I haved used 18 as the
partition limit. The interesting thing is that selection sort, will produce
more than one sublists containing 8 elements or less. 
"""

def quickSortMedian(alist):
    quickSortHelperMedian(alist, 0, len(alist) - 1)


def quickSortHelperMedian(alist, first, last):
    if first < last:  # Base Case, it will stop recurring when lenght is 1.

        # This will return the index of the pivot value.
        splitPoint = partitionMedian(alist, first, last)

        # This will apply the recursion to both sides once the pivot value is
        # exchanged with the split point.
        quickSortHelperMedian(alist, first, splitPoint - 1)
        quickSortHelperMedian(alist, splitPoint + 1, last)


def partitionMedian(alist, first, last):
    partitions = [alist[first], alist[last], alist[(last+first)//2]]
    pivotValue = statistics.median(partitions)
    if pivotValue == alist[last]:
        alist[first], alist[last] = alist[last], alist[first]
    elif pivotValue == alist[(last+first)//2]:
        alist[first], alist[(last+first)//2] = alist[(last+first)//2], alist[first]

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

# Median of three. method for selecting a pivot value as a modification to
# quickSort. Run an experiment to compare the two techniques.
