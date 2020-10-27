# To demonstrate that two loops nested iterating through n is O(n^2).
import numpy as np
from matplotlib import pyplot as plt
from timeit import Timer

x_axis = np.array([])
y_axis = np.array([])

for i in range(10, 1_001, 20):
    t = Timer("main()", "from __main__ import main")

    def main():
        for a in range(i):
            for b in range(i):
                continue

    time = t.timeit(number=1000)
    print("Range: {}, Time: {:.6f} miliseconds".format(i, time))
    x_axis = np.append(x_axis, i)
    y_axis = np.append(y_axis, time)

plt.plot(x_axis, y_axis, 'g^')
plt.xlabel("Range/Num of Elements")
plt.ylabel("Time(ms) to perform nesting iteration operation.")
plt.show()