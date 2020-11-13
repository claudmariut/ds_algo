from UnorderedList import UnorderedList

class StackLinkedList:
    """Represent a Stack using a linked list."""
    def __init__(self):
        self.items = UnorderedList()

    def push(self, item):
        self.items.add(item)

    def pop(self):
        item = self.items.head.getData()
        self.items.head = self.items.head.getNext()
        self.items.size -= 1
        return item

    def peek(self):
        return self.items.head.getData()

    def isEmpty(self):
        return self.items.head == None

    def size(self):
        return self.items.size
