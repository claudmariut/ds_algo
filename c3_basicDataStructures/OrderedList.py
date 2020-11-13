from Node import Node


class OrderedList:
    """Represent Ordered list with a particular order using linked list"""
    def __init__(self):
        self.head = None

    def isEmpty(self):
        """Return if head is linked to a node."""
        return self.head == None

    def length(self):
        """Returns length of Unordered List by "traversing"."""
        current = self.head
        counter = 0
        while current != None:
            current = current.getNext()
            counter += 1

        return counter

    def remove(self, item):
        """Remove existing item from list."""
        current = self.head
        previous = None
        found = False
        while not found:
            try:
                if current.getData() == item:
                    found = True
                else:
                    previous = current
                    current = current.getNext()
            except AttributeError:
                print("Error: Item not found.")
                break

        if found:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

    def search(self, item):
        """Returns True if item in list."""
        current = self.head
        found = False
        stop = False
        while not found and current != None and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def index(self, item):
        """Returns index of item in list."""
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

    def add(self, item):
        """Adds item to the list."""
        current = self.head
        previous = None
        stop = False
        while not stop and current != None:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp

        else:
            temp.setNext(current)
            previous.setNext(temp)

    def pop(self, pos=None):
        """Removes and return the element at certain index. Last by default."""
        current = self.head
        previous = None
        counter = 0
        position = pos

        if pos == None:
            length = self.length() - 1
            position = length

        while counter != position:
            previous = current
            current = current.getNext()
            counter += 1

        if previous == None:
            self.head = current.getNext()
            return current.getData()

        else:
            previous.setNext(current.getNext())
            return current.getData()

    def display(self):
        """Display linked list in a visual format."""
        current = self.head
        if current:
            print(f"Head--> |{current.getData()}|--> ", end="")
            while current.getNext() != None:
                print(f"|{current.next.getData()}|--> ", end="")
                current = current.next
            print(f"End")
