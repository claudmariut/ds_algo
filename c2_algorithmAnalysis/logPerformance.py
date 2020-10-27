# Prove the 0(log n) performance in an operation.
import timeit
from matplotlib import pyplot as plt
import numpy as np

x_axis = np.array([])
y_axis = np.array([])

for i in range(1_000, 1_000_001, 5_000):

    x_axis = np.append(x_axis, i)

    def main(i):
        while i > 0:
            k = 2 + 2
            i = i // 2

    t = timeit.Timer("main(i)", "from __main__ import main, i")
    time = t.timeit(number=1000)
    y_axis = np.append(y_axis, time)
    print("Range: {}, Time: {:.6f} (ms)".format(i, time))

plt.plot(x_axis, y_axis, '^g')
plt.show()