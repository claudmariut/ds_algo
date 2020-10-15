class Number:
    def __init__(self, n):
        self.num = n

    def getNum(self):
        return self.num

    def __add__(self, other):
        return self.num + other.num

    def __radd__(self, other):
        return self.num + other

    def __iadd__(self, other):
        self.num = self.num + other


n1 = Number(4)
n2 = Number(6)

print(5 + n1) # When x + y is evaluated. x.__add__(n1) and n1__radd__(y).
print(n1.__radd__(5))


class Magic:
    def __init__(self, label):
        self.label = label

    def __str__(self):
        return self.label

    def __repr__(self):
        return f"Magic({self.label})"


m1 = Magic("Representation")
print(repr(m1))  # unambiguous. Identifier, Class name, etc...
print(m1)  # Calls str, readable message.
