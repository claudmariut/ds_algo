from LinkedListQueue import linkedListQueue

# Asumes all the numbers are digit strings, given as a list and all have the
# number of characters.
alist = ["043", "723", "007", "104", "932", "580"]


def radixSort(listItems):
    bins = [linkedListQueue() for index in range(10)]  # Create ten bin queues.

    for x in range(1, len(listItems[0]) + 1):
        for bin in bins:
            while not bin.isEmpty():
                listItems.append(bin.dequeue())

        for num in listItems:
            index = num[-x]
            bins[int(index)].enqueue(num)
            listItems = []

    for bin in bins:
        while not bin.isEmpty():
            listItems.append(bin.dequeue())

    return listItems


print(radixSort(alist))