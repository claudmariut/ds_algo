class Node:
    """Represent a Node with reference to left and right."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def getData(self):
        """Return data of current node"""
        return self.data

    def getLeft(self):
        """Return left child"""
        return self.left

    def getRight(self):
        """Return right child"""
        return self.right

    def setLeft(self, child):
        """Link node with left child"""
        self.left = child

    def setRight(self, child):
        """Link node with right child"""
        self.right = child



