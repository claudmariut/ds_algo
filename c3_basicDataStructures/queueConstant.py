from LinkedListQueue import linkedListQueue
import numpy as np
import timeit
from matplotlib import pyplot as plt

x_axis = np.array([])
y_Dequeue = np.array([])
y_Enqueue = np.array([])
times = []

mySetup = "from queueConstant import q3"

for x in range(10_000, 1_00_000, 20_000):
    q3 = linkedListQueue()

    for y in range(x):
        q3.enqueue(y)

    time1 = timeit.timeit("q3.dequeue()", setup=mySetup, number=1000)
    time2 = timeit.timeit("q3.enqueue(0)", setup=mySetup, number=1000)
    times.append("Range: {}, Dequeue(): {:.6f}, Enqueue(): {:.6f}"
                       .format(x, time1, time2))

    x_axis = np.append(x_axis, x)
    y_Dequeue = np.append(y_Dequeue, time1)
    y_Enqueue = np.append(y_Enqueue, time2)


def showGraph():
    plt.plot(x_axis, y_Dequeue, "-k", label="O(1)")
    plt.plot(x_axis, y_Enqueue, "y--", label="O(1)")
    plt.legend()
    plt.ylim(top=0.020)
    plt.xlabel("Num of Elements in Queue")
    plt.ylabel("Time(ms) to perform dequeue()/enqueue() operations.")
    plt.show()

def showTimes():
    for time in times:
        print(time)



