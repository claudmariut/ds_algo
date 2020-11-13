from Node import Node


class UnorderedList:
    """Represent an unordered list / linked list build by nodes."""
    def __init__(self):
        """By default we set the head linked to nowherDelete Last − Deletes an element from the end of the list.e in the constructor."""
        self.head = None
        self.end = None
        self.size = 0

    def isEmpty(self):
        """Return if head is linked to a node."""
        return self.head == None

    def add(self, item):
        """Creates a node with the item value. Then link it to the head
        and then make it as the new head."""
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        if self.size == 0:
            self.size = 1
        else:
            self.size += 1

    def length(self):
        """Returns length of Unordered List by "traversing"."""
        return self.size

    def insert(self, pos, item):
        """Insert node at specific position."""
        if pos == 0:
            self.add(item)
        else:
            temp = Node(item)
            counter = 1
            current = self.head
            while counter != pos and current.next != None:
                current = current.next
                counter += 1

            temp.next = current.next
            current.next = temp
            self.size += 1

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

    def remove(self, item):
        """Removes existing item from linked list."""
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
                self.size = 0
            else:
                previous.setNext(current.getNext())
            self.size -= 1

    def append(self, item):
        """Appends item to the end of the list."""
        temp = Node(item)
        current = self.head
        if current == None:
            self.head = temp
            self.size = 1
        else:
            while current.getNext() != None:
                current = current.getNext()

            current.setNext(temp)
            self.size += 1


    def pop(self, pos=None):
        """Removes and returns item at position pos. Returns item."""
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
            self.size = 0
            return current.getData()

        else:
            previous.setNext(current.getNext())
            self.size -= 1
            return current.getData()



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

    def display(self):
        """Display linked list in a visual format."""
        current = self.head
        if current:
            print(f"Head--> |{current.getData()}|--> ", end="")
            while current.getNext() != None:
                print(f"|{current.next.getData()}|--> ", end="")
                current = current.next
            print(f"End")





