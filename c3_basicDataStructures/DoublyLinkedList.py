from Node2 import Node

class DoublyLinkedList:
    """Represend a doubly linked list."""
    def __init__(self):
        self.head = None
        self.traverse = []
        self.reverseTraverse = []
        self.size = 0

    def insertFront(self, item):
        """Adds an element at the head of the list."""
        if self.head == None:
            self.head = Node(item)
            self.head.prev = self.head
            self.size += 1

        else:
            temp = Node(item)
            temp.setNext(self.head)
            temp.setPrev(self.head.prev)
            self.head.prev = temp
            self.head = temp
            self.size += 1

    def insertEnd(self, item):
        """Adds an element at the end of the list."""
        if self.head == None:
            self.head = Node(item)
            self.head.prev = self.head
            self.size += 1

        else:
            temp = Node(item)
            last = self.head.getPrev()
            last.setNext(temp)
            temp.setPrev(last)
            self.head.setPrev(temp)
            self.size += 1

    def insert(self, pos, item):
        """Insert node at specific position."""
        if pos == 0:
            self.insertFront(item)
        else:
            temp = Node(item)
            counter = 1
            current = self.head
            while counter != pos and current.next != None:
                current = current.next
                counter += 1

            temp.next = current.next
            temp.prev = current
            current.getNext().setPrev(temp)
            current.next = temp
            self.size += 1

    def removeFront(self):
        """Remove an element from the front."""
        if self.size == 0:
            print("Can not remove from empty list.")
        elif self.size == 1:
            self.head = None
            self.size = 0
        else:
            self.head.getNext().setPrev(self.head.prev)
            self.head = self.head.getNext()
            self.size -= 1

    def removeEnd(self):
        """Remove and element from the end."""
        if self.size == 0:
            print("Can not remove from empty list.")
        elif self.size == 1:
            self.head = None
            self.size = 0
        else:
            last = self.head.getPrev()
            self.head.setPrev(last.getPrev())
            last.getPrev().next = None
            self.size -= 1

    def remove(self, item):
        """Removes item from the list."""
        if item == self.head.getPrev().getData():
            self.removeEnd()
        elif item == self.head.getData():
            self.removeFront()
        else:
            current = self.head
            found = False
            while not found:
                try:
                    if current.getData() == item:
                        found = True
                    else:
                        current = current.getNext()
                except AttributeError:
                    print("Error: Item not found.")
                    break
                else:
                    current.getPrev().setNext(current.getNext())
                    current.getNext().setPrev(current.getPrev())
                    self.size -= 1

    def index(self, item):
        """Returns index of item in list from head."""
        current = self.head
        counter = 0
        found = False
        while not found:
            if current.getData() == item:
                found = True

            else:
                current = current.getNext()
                counter += 1
        return counter

    def search(self, item):
        """Returns True if item in linked list."""
        current = self.head
        found = False
        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                current = current.next

        return found

    def displayForward(self):
        """Display list from head to end."""
        current = self.head
        if current:
            print(f"Head-->|{current.getData()}|", end="")
            while current.getNext() != None:
                print(f"<-->|{current.getNext().getData()}|", end="")
                current = current.getNext()
            print(f"-->End")
        if current:
            print(f"   |{current.getData()}|<-'")

    def displayBackward(self):
        """Display list from end to head."""
        last = self.head.getPrev()
        current = last
        if current:
            print(f"End<--|{current.getData()}|", end="")
            while current.getPrev() != last:
                print(f"<-->|{current.getPrev().getData()}|", end="")
                current = current.getPrev()
            print(f"<--Head")

    def getTraverse(self):
        """Return list in traversal."""
        current = self.head
        if current:
            self.traverse.append(current.getData())
            while current.getNext() != None:
                self.traverse.append(current.getNext().getData())
                current = current.getNext()
        return self.traverse

    def getReverseTraverse(self):
        """Return list in reverse traversal."""
        last = self.head.getPrev()
        current = last
        if current:
            self.reverseTraverse.append(current.getData())
            while current.getPrev() != last:
                self.reverseTraverse.append(current.getPrev().getData())
                current = current.getPrev()
        return self.reverseTraverse

