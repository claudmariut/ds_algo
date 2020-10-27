# Experiment to prove that del operation in list is O(n), and del operator
# in dictionary is O(1).

import timeit
import numpy as np
import random
from matplotlib import pyplot as plt

x_axis = np.array([])
y_lst = np.array([])
y_dic = np.array([])

for i in range(10_000, 1_000_001, 20_000):

    x_axis = np.append(x_axis, i)

    x = list(range(i))
    t1 = timeit.Timer("del x[random.randrange(len(x))]",
                      "from __main__ import x, random")
    lst_time = t1.timeit(number=1000)
    y_lst = np.append(y_lst, lst_time)

    x = {j: None for j in range(i)}
    t2 = timeit.Timer("del x[next(iter(x))]",
                      "from __main__ import x")
    dic_time = t2.timeit(number=1000)
    y_dic = np.append(y_dic, dic_time)

    print("Range: {}, List time: {:.6f}, Dictionary time: {:.6f}"
          .format(i, lst_time, dic_time))

plt.plot(x_axis, y_lst, '+b', x_axis, y_dic, '^r')
plt.ylabel("Time (ms) for del operation.")
plt.xlabel("Range")
plt.show()


