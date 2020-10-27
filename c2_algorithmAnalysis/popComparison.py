from timeit import Timer

popzero = Timer("x.pop(0)", "from __main__ import x")
popend = Timer("x.pop()", "from __main__ import x")

x = list(range(2000000))
print(popzero.timeit(number=1000))
print(popend.timeit(number=1000))

""".pop(i) is O(n), porque cada vez que un elemento es descartado del comienzo,
todos los elementos de la izquierda mueven una posicion. Si la lista contiene
2 millones de elementos, cuando un elemento del comienzo es descartado,
los 1.99 millones restantes indexan a la izquierda O(1)*1.99 veces.
Por lo tanto >> Si Index(1)*1.99 (n) = .pop(i) = O(1.99) o O(n)."""

"""Sin embargo, .pop() es O(1), porque cada vez que un elemento se descarta
del final, no se realiza ninguna accion extra."""

