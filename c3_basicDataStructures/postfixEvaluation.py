from Stack import Stack


def postfixEval(postfixExpr):
    operandStack = Stack()
    postfixList = postfixExpr.split()

    for token in postfixList:
        if token.isdigit():
            operandStack.push(int(token))

        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)

    return operandStack.pop()


def doMath(token, operand1, operand2):
    if token == "+":
        return operand1 + operand2
    elif token == "-":
        return operand1 - operand2
    elif token == "*":
        return operand1 * operand2
    elif token == "/":
        return operand1 / operand2


print(postfixEval("17 10 + 3 * 9 /"))

