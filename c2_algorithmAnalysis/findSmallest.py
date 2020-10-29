# Create a linear algorithm to find the smallest kth number given a random
# list.
import random
import timeit
import numpy as np
from matplotlib import pyplot as plt

times = []
x_axis = np.array([])
y_axis = np.array([])
y_axis2 = np.array([])
y_axis3 = np.array([])

for i in range(1_000, 10_001, 200):
    alist = [random.randint(1, 1_000_001) for x in range(i)]
    x_axis = np.append(x_axis, i)

    def main(l):
        min1 = l[0]
        for element in l:
            if element < min1:
                min1 = element

    t1 = timeit.Timer("main(alist)", "from findSmallest import main, alist")
    time1 = t1.timeit(number=1000)
    y_axis = np.append(y_axis, time1)

    def main2(l):
        min2 = min(l)

    t2 = timeit.Timer("main2(alist)", "from findSmallest import main2, alist")
    time2 = t2.timeit(number=1000)
    y_axis2 = np.append(y_axis2, time2)

    def main3(l):
        l.sort()
        min3 = l[0]

    t3 = timeit.Timer("main3(alist)", "from findSmallest import main3, alist")
    time3 = t3.timeit(number=1000)
    y_axis3 = np.append(y_axis3, time3)

    times.append("Range: {}, Time Algo: {:.6f} (ms), Time b-in: {:.6f},"
          " Time Algo2: {:.6f}".format(i, time1, time2, time3))


def showGraph():
    plt.plot(x_axis, y_axis, '^c', label="Iteration 0(n)")
    plt.plot(x_axis, y_axis2, '*r', label="Built-in min() function.")
    plt.plot(x_axis, y_axis3, '+g', label="Sort and return O(nlogn)")
    plt.legend()
    plt.show()


def showTimes():
    for time in times:
        print(time)

