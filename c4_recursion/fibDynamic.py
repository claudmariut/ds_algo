"""Recursion algorithm implementing dynamic programming using mimoization
to find  nth number in the fibonaci sequence in linear time O(2n)."""


class fibDynamic:
    def __init__(self):
        self.memoization = {}
        self.functionCalls = 0

    def fib(self, n):
        self.functionCalls += 1
        if n in self.memoization.keys():
            return self.memoization[n]
        if n == 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = self.fib(n - 1) + self.fib(n - 2)
        self.memoization[n] = result
        return result


# Dynamic programming takes 39 function calls to solve the problem for n = 20.
f = fibDynamic()
print(f.fib(20))
print("Number of function calls: ", end="")
print(f.functionCalls)
