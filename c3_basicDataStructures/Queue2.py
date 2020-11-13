class Queue2:
    """To implement Queue abstract data structure"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        """O(1)"""
        self.items.append(item)

    def dequeue(self):
        """O(n)"""
        return self.items.pop(0)

    def size(self):
        return len(self.items)

