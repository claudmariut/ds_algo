from Stack import Stack
import string

def infixToPostfix(infixExpr):
    # Stack containing operators.
    stackOp = Stack()
    # Dictionary containing operators as keys with precedence values.
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    tokenList = infixExpr.split()
    postfixList = []

    for token in tokenList:
        if token in string.ascii_uppercase:
            postfixList.append(token)

        elif token == "(":
            stackOp.push(token)

        elif token == ")":
            topToken = stackOp.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = stackOp.pop()

        else:
            while (not stackOp.isEmpty() and
                   prec[stackOp.peek()] >= prec[token]):
                postfixList.append(stackOp.pop())
            stackOp.push(token)

    while not stackOp.isEmpty():
        postfixList.append(stackOp.pop())

    return " ".join(postfixList)


print(infixToPostfix("A + ( B + ( C + D ) )"))




