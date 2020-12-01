class fibRecursion:
    def __init__(self):
        self.functionCalls = 0

    def fib(self, n):
        self.functionCalls += 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

# Recursion itself takes 22000 function calls to solve for n = 20.
f = fibRecursion()
print(f.fib(20))
print("Number of function calls: ", end="")
print(f.functionCalls)