from Stack import Stack


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                balanced = matches(symbol, top)


        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(close, open):
    front = "([{"
    end = ")]}"
    return front.index(open) == end.index(close)


print(parChecker("({([])})"))



