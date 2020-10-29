# Contains(in) operation List vs Dictionaries (as keys)
# To prove that contain operation in list is O(n), and contain operation in
# Dictionary is O(1).
import matplotlib.pyplot as plt
import numpy as np
from timeit import Timer
import random

times = []
x_axis = np.array([])
y_lst = np.array([])
y_dic = np.array([])

for i in range(10_000, 1_000_001, 20_000):
    t = Timer(f"random.randrange({i}) in x", "from containsComparison import random, x")

    x = list(range(i))
    lst_time = t.timeit(number=1000)
    y_lst = np.append(y_lst, lst_time)
    x = {j: None for j in range(i)}
    d_time = t.timeit(number=1000)
    y_dic = np.append(y_dic, d_time)
    times.append("Range : {}, List time:, {:.6f}, Dic time: {:.6f} (msec)."
                 .format(i, lst_time, d_time))
    x_axis = np.append(x_axis, i)


def showGraph():
    plt.plot(x_axis, y_lst, 'kD', label="List")
    plt.plot(x_axis, y_dic, 'c+', label="Dictionary")
    plt.xlabel("Range/Num of Elements")
    plt.ylabel("Time(ms) to perform contain-in operation.")
    plt.legend()
    plt.show()


def showTimes():
    for time in times:
        print(time)


""".randrange(start, stop, step), works the same as .randint. The differences
are that in randint, we can not user steps, and the range is inclusive [a, b],
in .randrange, the range is not inclusive, so b is not part of the range, but 
b - 1."""
# https://wiki.python.org/moin/TimeComplexity
