import random
from shellSort import *
import timeit
import numpy as np
from matplotlib import pyplot as plt

mySetup = "from shellComplexity import x, random, " \
          "shellSort"

x_axis = np.array([])
shell_axis = np.array([])
times = []

for x in range(50, 1_000_051, 50_000):

    timeshell = timeit.timeit("shellSort([random.randint(0, 10_000_000_000) "
                              "for i in range(x)])",
                            setup=mySetup, number=1)

    times.append("Range: {}, Shell: {:.6f}s".format(x, timeshell))

    x_axis = np.append(x_axis, x)
    shell_axis = np.append(shell_axis, timeshell)


def showTimes():
    for time in times:
        print(time)


def showGraph():
    plt.plot(x_axis, shell_axis, "--b", label="Shell")
    plt.legend()
    plt.xlabel("Range of list")
    plt.ylabel("Time(ms) to perform search operation.")
    plt.show()
