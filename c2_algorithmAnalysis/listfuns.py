"""Different ways to to generate a list of n numbers starting with 0."""
from timeit import Timer


# Concatenation.
def test1():
    l = []
    for i in range(1000):
        l = l + [i]


# Appending.
def test2():
    l = []
    for i in range(1000):
        l.append(i)


# List comprehension.
def test3():
    l = [i for i in range(1000)]


# List constructor with range function.
def test4():
    l = list(range(1000))


t1 = Timer("test1()", "from __main__ import test1")
print("Concat ", t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("Append ", t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("Comprehension ", t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("List range ", t4.timeit(number=1000), "milliseconds")


