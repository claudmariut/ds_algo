from Deque import Deque


def palindromeChecker(string):
    charDeque = Deque()
    for char in string:
        if char != " ":
            charDeque.addRear(char)

    stillEqual = True

    while charDeque.size() > 1 and stillEqual:
        if not charDeque.removeFront() == charDeque.removeRear():
            stillEqual = False

    return stillEqual


print(palindromeChecker("I PREFER PI"))
