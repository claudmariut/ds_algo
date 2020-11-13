from Stack import Stack


def prefixEval(prefixExpr):
    operandStack = Stack()
    prefixList = prefixExpr.split()
    prefixList.reverse()

    for token in prefixList:
        if token.isdigit():
            operandStack.push(int(token))

        else:
            operand1 = operandStack.pop()
            operand2 = operandStack.pop()
            operator = token
            result = doMath(operator, operand1, operand2)
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


print(prefixEval("/ 10 2"))