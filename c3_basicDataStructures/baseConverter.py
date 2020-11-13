# Using Stack data structure to convert a decimal number to binary.
# (Applicable to any base)

from Stack import Stack


def convertBase(decNumber, base):
    digits = "0123456789ABCDEF"
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber //= base

    newNumber = ""
    while not remstack.isEmpty():
        newNumber += digits[remstack.pop()]

    return newNumber





