from timeit import Timer
from matplotlib import pyplot as plt
import numpy as np

times = np.array([])
operation = np.array(["Checking Off", "Sort and Compare", "Brute Force",
                     "Count and Compare"])

s1 = Timer("anagramSolution1()", "from s1checkingOff import anagramSolution1")
t1 = s1.timeit(number=1000)
s2 = Timer("anagramSolution2()", "from s2sortCompare import anagramSolution2")
t2 = s2.timeit(number=1000)
s3 = Timer("anagramSolution3()", "from s3bruteForce import anagramSolution3")
t3 = s3.timeit(number=1000)
s4 = Timer("anagramSolution4()", "from s4countCompare import anagramSolution4")
t4 = s4.timeit(number=1000)

times = np.append(times, t1)
times = np.append(times, t2)
times = np.append(times, t3)
times = np.append(times, t4)


def showGraph():
    plt.bar(operation, times)
    plt.show()


def showTimes():
    for x in range(len(times)):
        print(operation[x], "=", times[x])

