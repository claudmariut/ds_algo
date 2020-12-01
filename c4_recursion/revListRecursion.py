def reverseList(alist):
    """Recursive algorith to reverse a list"""
    if len(alist) == 0 or len(alist) == 1:
        return alist
    elif len(alist) == 2:
        return [alist.pop(), alist.pop()]
    else:
        return reverseList(alist[1:]) + [alist[0]]


print(reverseList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
