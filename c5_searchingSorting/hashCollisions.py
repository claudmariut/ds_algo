def hash(item, tablesize):
    return item % tablesize

alist = [None] * 11
myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]

for item in myList:
    slotName = hash(item, len(alist))
    while alist[slotName] != None:
        slotName = (slotName + 1) % len(alist)

    alist[slotName] = item

# A cluster of items for slot 0.
print(alist)

alist = [None] * 11
for item in myList:
    slotName = hash(item, len(alist))
    while alist[slotName] != None:
        # To avoid clustering at slot 0. We use a technique for collision
        # resolution. "Plus 3" If slot is occupied. (Rehashing)
        slotName = (slotName + 3) % len(alist)

    alist[slotName] = item


# Collision resolution Using "Plus 3"
print(alist)

alist = [None] * 11
for item in myList:
    slotName = hash(item, len(alist))
    j = 1
    if alist[slotName] == None:
        alist[slotName] = item
    else:
        while True:
            # slotName is always the same, but new hash value is each time
            # and each is added to (j^2), where j starts at 1 and increments
            # by one each time.
            newhashvalue = (slotName + j ** 2) % len(alist)
            if alist[newhashvalue] == None:
                alist[newhashvalue] = item
                break
            else:
                j += 1

# Collision resolution with Quadratic Probing.
print(alist)

alist = [None] * 11
for item in myList:
    slotName = hash(item, len(alist))
    j = 1
    # If the slot is empty, then we create a list and append the item.
    if alist[slotName] == None:
        alist[slotName] = []
        alist[slotName].append(item)
    else:
        alist[slotName].append(item)


# Collision resolution with Chaining.
print(alist)


def find(item, alist):
    found = False
    slotName = hash(item, len(alist))
    for value in alist[slotName]:
        if value == item:
            found = True
            break

    return found

"""
The process of looking for another slot after a collision is called rehashing.
newhashvalue = rehas(oldhashvalue), where rehash(pos) = (pos + skip) % sizeotbl
It is recommended that the table size is a prime number so all the table will 
be visited.
"""

print(find(55, alist))

