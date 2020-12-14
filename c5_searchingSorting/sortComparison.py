import random
from bubbleSort import *
from selectionSort import *
from insertionSort import *
from shellSort import *
import timeit
import numpy as np
from matplotlib import pyplot as plt

mySetup = "from sortComparison import x, random, " \
          "bubbleSort, selectionSort, insertionSort, shellSort"

x_axis = np.array([])
bubble_axis = np.array([])
selection_axis = np.array([])
insertion_axis = np.array([])
shell_axis = np.array([])
times = []

for x in range(1, 50, 1):

    timebubble = timeit.timeit("bubbleSort([random.randint(0, 10_000_000_000) "
                               "for i in range(x)])",
                                setup=mySetup, number=1000)
    timeselection = timeit.timeit("selectionSort([random.randint(0, 10_000_000_000) "
                                  "for i in range(x)])",
                           setup=mySetup, number=1000)
    timeinsertion = timeit.timeit("insertionSort([random.randint(0, 10_000_000_000) "
                                  "for i in range(x)])",
                           setup=mySetup, number=1000)
    timeshell = timeit.timeit("shellSort([random.randint(0, 10_000_000_000) "
                              "for i in range(x)])",
                            setup=mySetup, number=1000)

    times.append("Range: {}, Bub: {:.6f}s, Sel: {:.6f}s, "
                 "Ins: {:.6f}s, Shell: {:.6f}s".format(x,
                        timebubble, timeselection, timeinsertion, timeshell))

    x_axis = np.append(x_axis, x)
    bubble_axis = np.append(bubble_axis, timebubble)
    selection_axis = np.append(selection_axis, timeselection)
    insertion_axis = np.append(insertion_axis, timeinsertion)
    shell_axis = np.append(shell_axis, timeshell)


def showTimes():
    for time in times:
        print(time)


def showGraph():
    plt.plot(x_axis, bubble_axis, "--y", label="Bubble")
    plt.plot(x_axis, selection_axis, "--g", label="Selection")
    plt.plot(x_axis, insertion_axis, "--k", label="Insertion")
    plt.plot(x_axis, shell_axis, "--b", label="Shell")
    plt.legend()
    plt.xlabel("Range of list")
    plt.ylabel("Time(ms) to perform search operation.")
    plt.show()
