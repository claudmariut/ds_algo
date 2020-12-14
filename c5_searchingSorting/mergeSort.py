def mergeSortSlicing(alist):
    if len(alist) > 1:  # Base case
        mid = len(alist) // 2  # Find middle point
        leftHalf = alist[:mid]  # Split list
        rightHalf = alist[mid:]

        mergeSortSlicing(leftHalf)  # Recursion call
        mergeSortSlicing(rightHalf)

        lidx = 0  # Left and right indexes.
        ridx = 0
        fidx = 0  # Final index in sublist.
        # Iterate through each sublists.
        while lidx < len(leftHalf) and ridx < len(rightHalf):
            if leftHalf[lidx] < rightHalf[ridx]:
                alist[fidx] = leftHalf[lidx]
                lidx += 1
            else:
                alist[fidx] = rightHalf[ridx]
                ridx += 1
            fidx += 1
        while lidx < len(leftHalf):
            alist[fidx] = leftHalf[lidx]
            lidx += 1
            fidx += 1
        while ridx < len(rightHalf):
            alist[fidx] = rightHalf[ridx]
            ridx += 1
            fidx += 1

# Work on this implementation.
"""
def mergeSort(alist, firstIndex, lastIndex):
    # Implementation without slicing.
    if lastIndex != firstIndex:  # Base case
        midIndex = ((firstIndex + lastIndex) + 1) // 2  # Find middle point

        mergeSort(alist, firstIndex, midIndex - 1)  # Recursion call
        mergeSort(alist, midIndex, lastIndex)

        lidx = firstIndex
        ridx = midIndex

        tmp = 0
        tmpList = []
        # Iterate through each sublists.
        while lidx < midIndex and ridx <= lastIndex:
            if (alist[lidx] < alist[ridx] and tmp == 0)\
                    or (tmp < alist[ridx] and tmp > 0):
                if tmp == 0:
                    lidx += 1
                    firstIndex += 1
                if tmp > 0:
                    if tmpList != []:
                        alist[firstIndex], tmp = tmp, tmpList.pop(0)
                    else:
                        alist[firstIndex], tmp = tmp, alist[firstIndex]
                    lidx += 1
                    firstIndex += 1
                    if lidx >= midIndex:
                        tmp = 0
            else:
                if tmp > 0:
                    if firstIndex < midIndex:
                        tmpList.append(alist[firstIndex])
                    alist[firstIndex] = alist[ridx]
                    ridx += 1
                    firstIndex += 1
                else:
                    tmp = alist[lidx]
                    alist[firstIndex] = alist[ridx]
                    ridx += 1
                    firstIndex += 1

        while lidx < midIndex:
            if tmp > 0:
                alist[firstIndex] = tmp
                tmp = 0
            else:
                alist[firstIndex] = lidx
            lidx += 1
            firstIndex += 1


myList = [random.randint(0, 1000) for x in range(200)]
mergeSort(myList, 0, len(myList) - 1)
print(myList)
"""

"""
Merge sort is a divide and conquer strategy. It splits the list in to parts
recursively. When it reaches a list of length 1, it starts building up again
sorting from sub-lists of size 1, to the list of size n. Using this approach
there are n comparisons for each level of depth. The number of levels is defined
by logn, with base 2. This is also the number of operations to slip a list of 
size n to a list of size 1. This means that the complexity for this aproach
is O(nlogn) which is pretty fast compared to the other alrogrithms discussed.
This algorithm requires more memory. 

The python implementation of this algorith uses slicing for each level. O(k) 
Notice, that we are splitting both sides. This basically means that it will take
n operations for each level. Or O(nlogn). If we take this into account, the
complexity of this implementation takes O(2nlogn) which is also O(nlogn).
"""