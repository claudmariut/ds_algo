import timeit
import random
from mergeSort import *
from quickSort import *
import numpy as np
from matplotlib import pyplot as plt

mySetup = "from mergequickComp import x, random, " \
          "quickSort, mergeSortSlicing"

x_axis = np.array([])
merge_axis = np.array([])
quick_axis = np.array([])

times = []

for x in range(1, 50, 1):

    timemerge = timeit.timeit("mergeSortSlicing([random.randint(0, 10_000_000_000) "
                               "for i in range(x)])",
                                setup=mySetup, number=1000)
    timequick = timeit.timeit("quickSort([random.randint(0, 10_000_000_000) "
                                  "for i in range(x)])",
                           setup=mySetup, number=1000)

    times.append("Range: {}, Merge: {:.6f}s, Quick: {:.6f}s".format(x,
                        timemerge, timequick))

    x_axis = np.append(x_axis, x)
    merge_axis = np.append(merge_axis, timemerge)
    quick_axis = np.append(quick_axis, timequick)



def showTimes():
    for time in times:
        print(time)


def showGraph():
    plt.plot(x_axis, merge_axis, "--m", label="Merge")
    plt.plot(x_axis, quick_axis, "--c", label="Quick")
    plt.legend()
    plt.xlabel("Range of list")
    plt.ylabel("Time(ms) to perform search operation.")
    plt.show()