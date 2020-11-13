from Queue1 import Queue
from Queue2 import Queue2
import timeit
import numpy as np
from matplotlib import pyplot as plt
"""Comparing two Queues implementation for enqueue/dequeue operations."""

mySetup = "from queueComparison import q1, q2"

x_axis = np.array([])
y_q1 = np.array([])
y_q2 = np.array([])
y_q3 = np.array([])
y_q4 = np.array([])
timeDequeue = []
timeEnqueue = []

for x in range(10_000, 100_000, 20_000):
    q1 = Queue()
    q2 = Queue2()

    for y in range(x):
        q1.enqueue(y)
        q2.enqueue(y)

    time1 = timeit.timeit("q1.dequeue()", setup=mySetup, number=1000)
    time2 = timeit.timeit("q2.dequeue()", setup=mySetup, number=1000)
    timeDequeue.append("Range: {}, Queue(): {:.6f}, Queue2(): {:.6f}"
                       .format(x, time1, time2))
    time3 = timeit.timeit("q1.enqueue(0)", setup=mySetup, number=1000)
    time4 = timeit.timeit("q2.enqueue(0)", setup=mySetup, number=1000)
    timeEnqueue.append("Range: {}, Queue(): {:.6f}, Queue2(): {:.6f}"
                       .format(x, time3, time4))

    x_axis = np.append(x_axis, x)
    y_q1 = np.append(y_q1, time1)
    y_q2 = np.append(y_q2, time2)
    y_q3 = np.append(y_q3, time3)
    y_q4 = np.append(y_q4, time4)


def showDequeueGraph():
    plt.plot(x_axis, y_q1, "-b", label="O(1)")
    plt.plot(x_axis, y_q2, "r--", label="O(n)")
    plt.legend()
    plt.xlabel("Num of Elements in Queue")
    plt.ylabel("Time(ms) to perform .dequeue() operation.")
    plt.show()


def showEnqueueGraph():
    plt.plot(x_axis, y_q3, "--g", label="O(n)")
    plt.plot(x_axis, y_q4, "b-", label="O(1)")
    plt.legend()
    plt.xlabel("Num of Elements in Queue")
    plt.ylabel("Time(ms) to perform .dequeue() operation.")
    plt.show()


def showEnqueueTimes():
    for time in timeEnqueue:
        print(time)


def showDequeueTimes():
    for time in timeDequeue:
        print(time)

