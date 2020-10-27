import time

# With Iteration.
def sumOfN(n):
    start = time.time()

    theSum = 0
    for i in range(1, n + 1):
        theSum = theSum + i

    end = time.time()
    return theSum, (end - start) * 1000


for i in range(5):
    print("Sum is %d required %10.7f miliseconds"%sumOfN(1_000_000))

print("------------------------------------------------------")


# W/0 Iteration.
def sumOfN3(n):
    start = time.time()
    return (n * (n + 1) / 2), (time.time() - start) * 1000


for i in range(5):
    print("Sum is %d required %10.7f miliseconds"%sumOfN3(1_000_000))

