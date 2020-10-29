from timeit import Timer
import numpy as np
from matplotlib import pyplot as plt

times = []
x_axis = np.array([])
y_pop0 = np.array([])
y_pop = np.array([])

for y in range(10_000, 1_000_001, 20_000):

    popzero = Timer("x.pop(0)", "from popComparison import x")
    popend = Timer("x.pop()", "from popComparison import x")

    x = list(range(y))
    tpop0 = popzero.timeit(number=1000)
    tpop = popend.timeit(number=1000)
    times.append("Range: {}, Pop(0): {:.6f}, Pop(): {:.6f}"
                 .format(y, tpop0, tpop))

    x_axis = np.append(x_axis, y)
    y_pop0 = np.append(y_pop0, tpop0)
    y_pop = np.append(y_pop, tpop)


def showGraph():
    plt.plot(x_axis, y_pop, "g--", label=".pop()")
    plt.plot(x_axis, y_pop0, "k*", label=".pop(0)")
    plt.xlabel("Range")
    plt.ylabel("Time (ms) to perform operation in list DS")
    plt.legend()
    plt.show()


def showTimes():
    for time in times:
        print(time)


""".pop(i) is O(n), porque cada vez que un elemento es descartado del comienzo,
todos los elementos de la izquierda mueven una posicion. Si la lista contiene
2 millones de elementos, cuando un elemento del comienzo es descartado,
los 1.99 millones restantes indexan a la izquierda O(1)*1.99 veces.
Por lo tanto >> Si Index(1)*1.99 (n) = .pop(i) = O(1.99) o O(n)."""

"""Sin embargo, .pop() es O(1), porque cada vez que un elemento se descarta
del final, no se realiza ninguna accion extra."""

