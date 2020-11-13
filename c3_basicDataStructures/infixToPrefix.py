from Stack import Stack
import string


def infixToPrefix(infixExpr):
    stackOp = Stack()
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec[")"] = 1
    prefixList = []
    infixList = infixExpr.split()
    infixList.reverse()

    for token in infixList:
        if token in string.ascii_uppercase:
            prefixList.append(token)

        elif token == ")":
            stackOp.push(token)

        elif token == "(":
            topToken = stackOp.pop()
            while topToken != ")":
                prefixList.append(topToken)
                topToken = stackOp.pop()

        else:
            while (not stackOp.isEmpty() and
                   prec[stackOp.peek()] > prec[token]):
                prefixList.append(stackOp.pop())
            stackOp.push(token)

    while not stackOp.isEmpty():
        prefixList.append(stackOp.pop())

    prefixList.reverse()
    return " ".join(prefixList)


print(infixToPrefix("( A + B ) * ( C + D )"))