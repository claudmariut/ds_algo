# FIFO first in, first out.

class Queue:
    """To implement Queue abstract data structure"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        """O(n)"""
        self.items.insert(0, item)

    def dequeue(self):
        """O(1)"""
        return self.items.pop()

    def size(self):
        return len(self.items)


"""
q = Queue()
print(q.isEmpty())
q.enqueue("Dog")
q.enqueue(4)
q.enqueue(True)
print(q.size())
print(q.isEmpty())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.size())
"""