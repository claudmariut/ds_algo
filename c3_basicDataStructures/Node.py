class Node:
    """Represent a node containing a data field and a reference to the next."""
    def __init__(self, initdata):
        self.data = initdata
        self.next = None  # We "ground" next. No pointing other node.

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

