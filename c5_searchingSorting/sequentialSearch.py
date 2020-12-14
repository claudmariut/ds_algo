# Sequential/linear search for unordered list.
def unorderedSequentialSearch(alist, item):
    # Index start at 0
    pos = 0
    found = False
    # Search through the list until found or end of list.
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1

    return found


# Sequential/linear search for ordered list.
def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1

    return found


"""
Both sequential searches present the same complexity of O(n) if the item is
present. The only difference is that, for the ordered list, if the item is not
present, the average case will be n/2. But again, as n gets larger, these
differences become less significant.
"""