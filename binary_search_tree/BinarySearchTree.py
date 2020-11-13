from Node import Node


class BST:
    """Represent a binary tree ordered by values. (-/+)"""
    def __init__(self):
        self.root = None
        self.preOrder = []
        self.inOrder = []
        self.postOrder = []

    def setRoot(self, initdata):
        """Set the root node"""
        self.root = Node(initdata)

    def insert(self, data):
        """Insert data to proper place."""
        current = self.root
        if current == None:
            self.root = Node(data)

        else:
            left = False
            right = False
            already = False
            previous = None
            while current != None:
                if data < current.getData():
                    previous = current
                    left = True
                    right = False
                    current = current.getLeft()
                elif data > current.getData():
                    previous = current
                    left = False
                    right = True
                    current = current.getRight()
                else:
                    print("Error: Value already defined.")
                    already = True
                    break

            if not already:
                if left:
                    previous.setLeft(Node(data))

                else:
                    previous.setRight(Node(data))

    def search(self, item):
        """Return if item in bst."""
        

    def setPreOrder(self):
        """Set bst in Pre-Order Traversal."""
        current = self.root
        if current != None:
            self.nlr(current)
        else:
            return "Error: Empty Tree."

    def nlr(self, current):
        """Node - Left - Right Policy."""
        self.preOrder.append(current.getData())
        visited = current
        if current.getLeft() != None:
            self.nlr(current.getLeft())
        if current.getRight() != None:
            self.nlr(current.getRight())

    def getPreOrder(self):
        """Return Pre Order Traversal."""
        if self.preOrder == []:
            self.setPreOrder()
            return self.preOrder
        else:
            return self.preOrder

    def setInOrder(self):
        """Set bst in In-Order Traversal."""
        current = self.root
        if current != None:
            self.lnr(current)
        else:
            return "Error: Empty Tree."

    def lnr(self, current):
        """Left - Node - Right Policy."""
        if current.getLeft() != None:
            self.lnr(current.getLeft())
        self.inOrder.append(current.getData())
        if current.getRight() != None:
            self.lnr(current.getRight())

    def getInOrder(self):
        """Return In Order Traversal."""
        if self.inOrder == []:
            self.setInOrder()
            return self.inOrder
        else:
            return self.inOrder

    def setPostOrder(self):
        """Set bst in Post-Order Traversal."""
        current = self.root
        if current != None:
            self.lrn(current)
        else:
            return "Error: Empty Tree."

    def lrn(self, current):
        """Left - Right - Node Policy"""
        if current.getLeft() != None:
            self.lrn(current.getLeft())
        if current.getRight() != None:
            self.lrn(current.getRight())
        self.postOrder.append(current.getData())

    def getPostOrder(self):
        """Return Post Order Traversal"""
        if self.postOrder == []:
            self.setPostOrder()
            return self.postOrder
        else:
            return self.postOrder
