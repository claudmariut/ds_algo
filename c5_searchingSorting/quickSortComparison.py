import timeit
import random
from quickSortTech import *
from quickSort import *
import numpy as np
from matplotlib import pyplot as plt

mySetup = "from quickSortComparison import x, random, " \
          "quickSortInsertion, quickSortMedian, quickSort"

x_axis = np.array([])
quickIns_axis = np.array([])
quick_axis = np.array([])
quickMed_axis = np.array([])

times = []

for x in range(1, 1000, 50):

    timequickIns = timeit.timeit("quickSortInsertion([i "
                               "for i in range(x)])",
                                setup=mySetup, number=100) * 10
    timequick = timeit.timeit("quickSort([i "
                                  "for i in range(x)])",
                           setup=mySetup, number=100) * 10
    timequickMed = timeit.timeit("quickSortMedian([i "
                              "for i in range(x)])",
                              setup=mySetup, number=100) * 10

    times.append("Range: {}, QuickIns: {:.6f}ms, Quick: {:.6f}ms, "
                 "QuickMed: {:.6f}ms".format(x, timequickIns, timequick,
                                           timequickMed))

    x_axis = np.append(x_axis, x)
    quickIns_axis = np.append(quickIns_axis, timequickIns)
    quick_axis = np.append(quick_axis, timequick)
    quickMed_axis = np.append(quickMed_axis, timequickMed)



def showTimes():
    for time in times:
        print(time)


def showGraph():
    plt.plot(x_axis, quickIns_axis, "--y", label="Quick Insertion")
    plt.plot(x_axis, quick_axis, "--c", label="Quick")
    plt.plot(x_axis, quickMed_axis, "--k", label="Quick Median")
    plt.legend()
    plt.xlabel("Range of list")
    plt.ylabel("Time(ms) to perform search operation.")
    plt.show()