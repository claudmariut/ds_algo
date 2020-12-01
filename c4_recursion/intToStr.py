from Stack import Stack


def toStr(n, base):
    """Change integer number to string in given base."""
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]


rStack = Stack()


def toStrStack(n, base):
    """Change integer number to string in given base using stack adt"""
    convertString = "01233456789ABCDEF"
    if n < base:
        rStack.push(convertString[n])
    else:
        rStack.push(convertString[n % base])
        toStrStack(n // base, base)


toStrStack(10, 2)
string = ""
while not rStack.isEmpty():
    string += rStack.pop()

print(string)
