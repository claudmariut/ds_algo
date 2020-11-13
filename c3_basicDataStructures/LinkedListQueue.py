"""Represent a Queue with O(1) enqueue and dequeue operations."""
from UnorderedList import UnorderedList, Node


class linkedListQueue:
    def __init__(self):
        self.items = UnorderedList()

    def enqueue(self, item):
        if self.items.head == None:
            self.items.head = Node(item)
            self.items.end = self.items.head

        else:
            previous = self.items.end
            self.items.end = Node(item)
            previous.setNext(self.items.end)

    def dequeue(self):
        item = self.items.head.getData()
        self.items.head = self.items.head.getNext()
        return item

    def isEmpty(self):
        """Return if head is linked to a node."""
        return self.items.head == None

    def size(self):
        """Returns length of Unordered List by "traversing"."""
        return self.items.size





