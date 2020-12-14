import random
from binarySearch import *
import timeit
import numpy as np
from matplotlib import pyplot as plt

mySetup = "from bsComparison import alist, x, random, " \
          "binarySearchRecursion, binarySearchSRec, binarySearchIterative"

x_axis = np.array([])
iter_axis = np.array([])
recS_axis = np.array([])
recI_axis = np.array([])
times = []

for x in range(1000, 1_000_000, 20_000):
    alist = [i for i in range(x)]

    timeiter = timeit.timeit("binarySearchIterative(alist, "
                           "random.randrange(0, 2 * x))",
                           setup=mySetup, number=100) * 10
    timerecS = timeit.timeit("binarySearchSRec(alist, "
                           "random.randrange(0, 2 * x))",
                           setup=mySetup, number=100) * 10
    timerecI = timeit.timeit("binarySearchRecursion(alist, "
                           "random.randrange(0, 2 * x), 0, len(alist) -1 )",
                           setup=mySetup, number=100) * 10

    times.append("Range: {}, Iter: {:.6f}ms, Rec Sliced: {:.6f}ms, "
                 "Rec Index: {:.6f}".format(x, timeiter, timerecS, timerecI))

    x_axis = np.append(x_axis, x)
    iter_axis = np.append(iter_axis, timeiter)
    recS_axis = np.append(recS_axis, timerecS)
    recI_axis = np.append(recI_axis, timerecI)


def showTimes():
    for time in times:
        print(time)


def showGraph():
    plt.plot(x_axis, iter_axis, "^y", label="Iterative")
    plt.plot(x_axis, recS_axis, "*g", label="Recursion Sliced")
    plt.plot(x_axis, recI_axis, "--k", label="Recursion Index")
    plt.legend()
    plt.xlabel("Range of list")
    plt.ylabel("Time(ms) to perform search operation.")
    plt.show()

