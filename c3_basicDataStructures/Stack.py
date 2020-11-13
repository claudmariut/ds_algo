# Stack class assumes the end of the list will hold the top of the stack.
# So push() and pop() will both be O(1)
# LIFO last-in first-out.

class Stack:
    """Class to represent Stack ADT's implementing a data structures."""
    def __init__(self):
        """Constructror, create empty stack using list data structure."""
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

"""
s = Stack()
print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
print(s.items)
"""

