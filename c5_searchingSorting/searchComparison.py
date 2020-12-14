import random
from sequentialSearch import *
from binarySearch import *
import timeit
import numpy as np
from matplotlib import pyplot as plt

mySetup = "from searchComparison import alist, x, random, " \
          "orderedSequentialSearch, binarySearchRecursion"

x_axis = np.array([])
ss_axis = np.array([])
bs_axis = np.array([])
times = []

for x in range(1000, 1_000_000, 20_000):
    alist = [i for i in range(x)]

    timess = timeit.timeit("orderedSequentialSearch(alist, "
                           "random.randrange(0, 2 * x))",
                           setup=mySetup, number=100) * 10
    timebs = timeit.timeit("binarySearchRecursion(alist, "
                           "random.randrange(0, 2 * x), 0, len(alist) -1 )",
                           setup=mySetup, number=100) * 10

    times.append("Range: {}, SS: {:.6f}ms, BS: {:.6f}ms".format(x, timess, timebs))
    x_axis = np.append(x_axis, x)
    ss_axis = np.append(ss_axis, timess)
    bs_axis = np.append(bs_axis, timebs)


def showTimes():
    for time in times:
        print(time)


def showGraph():
    plt.plot(x_axis, ss_axis, "-b", label="Sequential Search")
    plt.plot(x_axis, bs_axis, "r--", label="Binary Search")
    plt.legend()
    plt.xlabel("Range of list")
    plt.ylabel("Time(ms) to perform search operation.")
    plt.show()
